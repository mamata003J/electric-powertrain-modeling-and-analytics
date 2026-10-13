# data_generator.py
# makes dummy data for the dashboard

import numpy as np
import pandas as pd


def generate_dummy_data():

    t = np.arange(0, 1800, 1)

    # dummy speed profile using 3 sine waves
    speed = 50 + 25*np.sin(2*np.pi*t/250) + 15*np.sin(2*np.pi*t/400) + 10*np.sin(2*np.pi*t/180)
    speed = np.clip(speed, 0, 130)

    # car parameters from Pratibha's sheet
    mass = 1600
    Cd = 0.29
    A = 2.3
    Crr = 0.010
    wheel_r = 0.35
    eta = 0.96 * 0.96 * 0.90

    # km/h to m/s
    v = speed / 3.6
    accel = np.gradient(v)

    # forces on the car
    F = Crr*mass*9.81 + 0.5*1.225*Cd*A*v**2 + mass*accel

    # power at wheels
    P = F * v

    # regen braking recovers 60 percent
    P = np.where(P < 0, P*0.6, P)

    # battery power with efficiency losses
    P_bat = np.where(P >= 0, P/eta, P*eta)

    # voltage and current (Sajib formula: P = V x I)
    V = 407 + 5*np.sin(2*np.pi*t/500)
    I = P_bat / V

    # motor rpm and torque (Sajib formula: P = T x omega)
    rpm = (v / wheel_r) * 60 / (2*np.pi)
    w = rpm * 2 * np.pi / 60
    torque = np.where(w > 1, P/np.maximum(w,1), 0)
    torque = np.clip(torque, -343, 343)

    # soc from energy (Sajib formula: E = integral of P)
    energy = np.cumsum(P_bat) / 3600
    soc = 100 - (energy / 94000) * 100
    soc = np.clip(soc, 0, 100)

    # efficiency (Sajib formula: output / input)
    # separate formula for driving and regen
    eff_drive = np.where(P_bat > 100, (P/P_bat)*100, 0)
    eff_regen = np.where(P_bat < -100, (P_bat/P)*100, 0)
    eff = np.clip(eff_drive + eff_regen, 0, 100)

    # build data table
    df = pd.DataFrame({
        'time': t,
        'speed': speed,
        'voltage': V,
        'current': I,
        'power': P_bat / 1000,
        'soc': soc,
        'rpm': rpm,
        'torque': torque,
        'efficiency': eff,
        'energy': np.maximum(energy, 0) / 1000,
    })

    return df


if __name__ == "__main__":
    df = generate_dummy_data()
    print(df.head())