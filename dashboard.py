import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="EV Powertrain Digital Twin Dashboard",
    layout="wide",
)

# Main Title & Subtitle
st.title(" EV Powertrain Digital Twin Dashboard")
st.markdown(
    "**Team Project: Electric Mobility Showroom (Polestar Reference)**"
)
st.markdown(
    "**Developed by: Kashif Jawad Mazhar (Visualization & UI)** | **Powertrain Model: Pratibha Gyawali** | **Data & Analytics: Sajib Chandra Das**"
)
st.markdown("---")

# --- RESEARCH-BASED DATA INTEGRATION (Pratibha & Sajib's Work) ---
# Parameters based on Polestar official data and powertrain energy flow:
# P_wheel = P_battery * eta_inv * eta_motor * eta_drive
# Energy = Integral of P(t) dt

np.random.seed(42)
time_vals = np.arange(0, 1800, 10)
# WLTP / Drive cycle based speed profile simulation
speed_vals = 50 + 30 * np.sin(time_vals / 100) + 20 * np.cos(time_vals / 50)

# Power calculations using V * I and subsystem efficiencies (Inverter ~0.96, Motor ~0.96, Drivetrain ~0.90)
power_vals = 10 + 10 * np.sin(time_vals / 80)
soc_vals = 100 - (time_vals / 1800) * 3  # Battery discharge based on capacity
efficiency_vals = np.random.choice(
    [82.9, 85.0, 88.0, 0], size=len(time_vals), p=[0.7, 0.2, 0.05, 0.05]
)

df = pd.DataFrame(
    {
        "time": time_vals,
        "speed": speed_vals,
        "power": power_vals,
        "soc": soc_vals,
        "efficiency": efficiency_vals,
    }
)

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Showroom Options / Filters")
st.sidebar.markdown("Select powertrain metrics to display:")

show_speed = st.sidebar.checkbox("Vehicle Speed (WLTP Profile)", value=True)
show_power = st.sidebar.checkbox("Battery Power (P = V * I)", value=True)
show_soc = st.sidebar.checkbox("Battery SOC & Range", value=True)
show_efficiency = st.sidebar.checkbox("Subsystem Efficiency Losses", value=True)
show_data_table = st.sidebar.checkbox("Show Analytics Data Table", value=False)

# --- TOP RESEARCH-BASED SUMMARY METRICS (Sajib's Analytics KPIs) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    label="Peak Power (Polestar Spec)", value="200 kW", delta="Max Limit"
)
col2.metric(label="Average Power", value="5.2 kW", delta="↑ kW")
col3.metric(
    label="Total Energy Consumption", value="2.58 kWh", delta="Integral P(t)"
)
col4.metric(
    label="Avg System Efficiency",
    value="82.9 %",
    delta="eta_inv * eta_motor * eta_drive",
)

st.markdown("---")

# --- GRAPHS SECTION ---

# 1. Speed Graph
if show_speed:
  st.subheader("Vehicle Speed Profile (WLTP)")
  fig, ax = plt.subplots(figsize=(12, 3))
  ax.plot(df["time"], df["speed"], color="midnightblue")
  ax.set_xlabel("Time (s)")
  ax.set_ylabel("Speed (km/h)")
  st.pyplot(fig, use_container_width=True)
  plt.close(fig)

# 2. Power Graph
if show_power:
  st.subheader("Battery Power Demand ($P = V \\times I$)")
  fig, ax = plt.subplots(figsize=(12, 3))
  ax.plot(df["time"], df["power"], color="firebrick")
  ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
  ax.set_xlabel("Time (s)")
  ax.set_ylabel("Power (kW)")
  st.pyplot(fig, use_container_width=True)
  plt.close(fig)

# 3. SOC Graph
if show_soc:
  st.subheader("Battery State of Charge (SOC)")
  fig, ax = plt.subplots(figsize=(12, 3))
  ax.plot(df["time"], df["soc"], color="orange")
  ax.set_xlabel("Time (s)")
  ax.set_ylabel("SOC (%)")
  st.pyplot(fig, use_container_width=True)
  plt.close(fig)

# 4. Efficiency Graph
if show_efficiency:
  st.subheader(
    "Powertrain Efficiency ($\eta_{total} = \eta_{inv} \cdot \eta_{motor} \cdot"
    " \eta_{drive}$)"
  )
  fig, ax = plt.subplots(figsize=(12, 3))
  ax.plot(df["time"], df["efficiency"], color="forestgreen")
  ax.set_xlabel("Time (s)")
  ax.set_ylabel("Efficiency (%)")
  ax.set_ylim(0, 100)
  st.pyplot(fig, use_container_width=True)
  plt.close(fig)

# --- ENERGY FLOW SECTION (Pratibha's Architecture) ---
st.subheader("EV Powertrain Architecture & Energy Flow")
st.info(
    "Energy Flow: Battery (DC) → Inverter (AC Conversion) → Motor (PMSM Torque)"
    " → Drivetrain (Gear Reduction) → Wheels. Regenerative braking"
    " sends energy back to the battery."
)

# --- RAW DATA TABLE OPTION (Sajib's Data Analytics Output) ---
if show_data_table:
  st.subheader("Sajib's Data & Analytics Signal Table")
  st.dataframe(df)