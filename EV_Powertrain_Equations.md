# EV Powertrain Model: Equation Documentation

Backward-facing (quasi-static) model. The drive cycle dictates speed; the model
works backward to find the power drawn from the battery.

```
Drive cycle -> Road load -> Wheel -> Gearbox -> Motor -> Inverter -> Battery
```

## 1. Symbols

| Symbol | Meaning | Unit | Typical value |
|---|---|---|---|
| m | Vehicle mass (incl. driver) | kg | 1500-2000 |
| m_eq | Equivalent mass incl. rotating inertia | kg | 1.03-1.05 m |
| g | Gravity | m/s² | 9.81 |
| ρ | Air density | kg/m³ | 1.2 |
| C_rr | Rolling resistance coefficient | - | 0.008-0.012 |
| C_d | Drag coefficient | - | 0.23-0.30 |
| A | Frontal area | m² | 2.2-2.4 |
| r | Wheel radius | m | 0.30-0.35 |
| G | Total gear ratio | - | 7-10 |
| η_g, η_m, η_inv | Gearbox, motor, inverter efficiency | - | 0.97, 0.92, 0.97 |
| v, a | Vehicle speed, acceleration | m/s, m/s² | from drive cycle |
| θ | Road slope | rad | 0 |
| V_oc, R | Battery open-circuit voltage, internal resistance | V, Ω | 300-400, 0.05-0.1 |
| Q_Ah | Battery capacity | Ah | 40-100 |

## 2. Road load at the wheels

```
F_roll  = C_rr · m · g · cos(θ)
F_aero  = ½ · ρ · C_d · A · v²
F_grade = m · g · sin(θ)
F_inert = m_eq · a
F_trac  = F_roll + F_aero + F_grade + F_inert
```

- F_roll is set to zero when the vehicle is stationary.
- m_eq = m + J_rot / r². If J_rot is unknown, use m_eq ≈ 1.04 · m.
- Acceleration comes from the drive cycle: a = dv/dt (numerical gradient).
- Convert speed first: v [m/s] = v [km/h] / 3.6.

## 3. Wheel to motor

```
T_wheel = F_trac · r
ω_wheel = v / r
ω_motor = ω_wheel · G
```

Motor torque (sign convention: positive = traction, negative = regen):

```
Traction (T_wheel >= 0):  T_motor = T_wheel / (G · η_g)
Regen    (T_wheel <  0):  T_motor = T_wheel · η_g / G
```

**Motor limits** (constant-torque region, then constant-power region):

```
T_max(ω) = min( T_peak , P_peak / ω_motor )
-T_max <= T_motor <= T_max
```

If the required torque exceeds T_max, the vehicle cannot follow the cycle at that
instant. The script counts these samples as `clipped_samples`.

**Regen rules**
- No regen below ~5 km/h (T_motor = 0).
- Charge power capped: P_dc >= -P_regen_max.
- Any braking demand not covered by regen is taken by friction brakes.

## 4. Power chain

```
P_mech = T_motor · ω_motor

Traction (P_mech >= 0):  P_dc = P_mech / (η_m · η_inv)
Regen    (P_mech <  0):  P_dc = P_mech · η_m · η_inv      (negative)

P_batt = P_dc + P_aux
```

Start with constant efficiencies, then replace with efficiency maps
η_m(T, ω) and η_inv(T, ω) using 2-D interpolation.

## 5. Battery: Rint model

```
V_oc(SOC) = V_min + (V_max - V_min) · SOC          (linear approximation)

P_batt = V_term · I = (V_oc - R·I) · I

I      = [ V_oc - sqrt( V_oc² - 4·R·P_batt ) ] / (2R)
V_term = V_oc - R · I

SOC(t+Δt) = SOC(t) - I · Δt / (3600 · Q_Ah)
```

- I > 0 discharge, I < 0 charge.
- If V_oc² < 4·R·P_batt the requested power is unreachable; the script clamps the
  discriminant to zero.
- Real cells have a nonlinear V_oc(SOC) curve and temperature-dependent R. Replace
  them with lookup tables when data is available.

## 6. Output metrics

```
Distance         = ∫ v dt                         [km]
Net energy       = ∫ P_batt dt / 3600             [Wh]
Regen energy     = -∫ min(P_batt, 0) dt / 3600    [Wh]
Consumption      = Net energy / Distance          [Wh/km]
Regen share      = Regen energy / Drive energy    [%]
```

Sanity check: typical passenger EVs give roughly 140-180 Wh/km on WLTP.

## 7. Forward-facing version (later extension)

A driver model generates the torque request instead of the cycle dictating
acceleration:

```
m_eq · dv/dt = F_trac_available - F_roll - F_aero - F_grade - F_brake
F_trac_available = T_motor · G · η_g / r
T_request = PI( v_ref - v )
```

This allows dynamic effects, driver behaviour and real controller testing, which
is useful for the digital twin.

## 8. Assumptions and limitations

1. Constant component efficiencies (no maps yet).
2. Linear V_oc(SOC); no thermal, aging or RC (transient) battery dynamics.
3. Single-speed gearbox; no slip or wheel dynamics.
4. Flat road unless a slope profile is supplied.
5. Auxiliary load is constant.
6. Friction braking is not modelled beyond the regen limit.
7. The built-in cycle is WLTP-like, not the official WLTP data.

## 9. Interface for teammates (suggested signal names)

| Signal | Symbol | Unit |
|---|---|---|
| `t` | time | s |
| `v_kmh` | speed | km/h |
| `T_m` | motor torque | Nm |
| `w_m` | motor speed | rad/s |
| `P_mech` | shaft power | W |
| `P_batt` | battery power | W |
| `I`, `V` | battery current, voltage | A, V |
| `soc` | state of charge | 0-1 |
