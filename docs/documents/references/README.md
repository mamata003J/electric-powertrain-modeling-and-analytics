# Project References

This folder contains the main academic and technical references used in the project:

**Electric Powertrain Modeling, Energy Analytics and Pilot Design**

The purpose of this literature collection is to support the design and development of an electric-vehicle powertrain digital twin, including:

- EV powertrain system modeling
- longitudinal vehicle dynamics
- battery, motor, inverter and drivetrain modeling
- regenerative braking
- energy-consumption analysis
- real-world vehicle data acquisition and analytics
- digital-twin architecture
- simulation validation
- pilot and visualization development

These papers form the initial **core literature base** of the project.

---

## Core Research Papers

### 1. Application of Digital Twin in Electric Vehicle Powertrain: A Review

**Authors:** Xiaokang Li, Wenxu Niu, Haobin Tian  
**Year:** 2024  
**Journal:** World Electric Vehicle Journal  
**DOI:** 10.3390/wevj15050208

### Role in this project

This paper is the main reference for the **digital-twin concept and architecture**.

It is used to understand:

- digital twin principles
- physical and virtual system interaction
- EV powertrain digital twins
- battery digital twins
- electric motor digital twins
- power-electronics digital twins
- real-time monitoring
- data synchronization
- challenges and future development of EV digital twins

This reference will mainly support the later stages of the project when the simulation model is connected with measured or real-world data.

---

### 2. Electric Vehicle Energy Consumption Modelling and Estimation—A Case Study

**Authors:** Ilyès Miri, Abbas Fotouhi, Nathan Ewin  
**Year:** 2021  
**Journal:** International Journal of Energy Research  
**DOI:** 10.1002/er.5700

### Role in this project

This is one of the most important references for the **physics-based EV simulation model**.

The paper develops an EV model in MATLAB/Simulink containing:

- driving cycle
- driver model
- longitudinal vehicle dynamics
- electric motor
- inverter / power electronics
- transmission
- battery model
- regenerative braking
- auxiliary loads
- energy-consumption estimation
- model validation

This paper will be used as a major reference when developing our own EV powertrain simulation architecture.

---

### 3. Data-Driven Analysis of Electric Powertrain Energy Flow and Traction Battery Behavior in a Modern Battery Electric Vehicle Using Real-World OBD Data

**Authors:** Jacek Caban, Branislav Šarkan, Arkadiusz Małek, Szymon Dowkontt, Michal Loman  
**Year:** 2026  
**Journal:** Electronics  
**DOI:** 10.3390/electronics15102018

### Role in this project

This paper is the main reference for the **data analytics and real-world vehicle-data layer**.

The study uses real OBD measurements from a battery electric vehicle and analyzes signals including:

- traction power
- battery current
- battery voltage
- battery state of charge
- accelerator pedal position
- battery temperature
- regenerative braking
- cell voltage imbalance

The methodology includes:

- data preprocessing
- timestamp synchronization
- signal filtering
- power and energy reconstruction
- operating-mode segmentation
- regression analysis
- visualization

This reference is particularly important for the transition from a simulation model toward a **data-connected digital-twin pilot**.

---

### 4. Modeling Techniques for Electric Vehicle Powertrains: A Comparative Review and Future Insights

**Authors:** Bassam Adel, Mohamed M. A. Hassan  
**Year:** 2025  
**Journal:** AIMS Energy  
**DOI:** 10.3934/energy.2025054

### Role in this project

This paper is used to help select the appropriate **modeling level and modeling techniques**.

It reviews different EV and battery modeling approaches, including:

- mathematical models
- electrical equivalent-circuit models
- electrochemical models
- reduced-order models
- data-driven models
- hybrid models

The paper also discusses the trade-off between:

- accuracy
- computational complexity
- real-time capability
- model interpretability
- available experimental data

This reference will help justify why the first version of our digital twin uses relatively simple and computationally efficient models before adding more advanced models.

---

### 5. Energy-optimal Design and Control of Electric Powertrains under Motor Thermal Constraints

**Authors:** Mouleeswar Konda, Theo Hofman, Mauro Salazar  
**Year:** 2022

### Role in this project

This paper provides an advanced reference for **electric powertrain architecture, energy flow and component losses**.

The modeled powertrain includes:

- battery
- inverter
- electric motor
- gearbox
- final drive
- wheels
- regenerative braking
- motor losses
- motor thermal behavior
- cooling system

It also includes longitudinal vehicle dynamics considering:

- aerodynamic drag
- rolling resistance
- road gradient
- vehicle inertia

This paper will mainly support advanced stages of the project, particularly if thermal modeling, loss optimization or more detailed motor modeling is included.

---

# How the References Support the Project

| Project Area | Main Reference |
|---|---|
| Digital twin concept | Li et al. |
| EV system architecture | Miri et al. / Konda et al. |
| Longitudinal vehicle dynamics | Miri et al. / Konda et al. |
| Motor and inverter modeling | Miri et al. / Konda et al. |
| Battery modeling | Adel & Hassan / Miri et al. |
| Regenerative braking | Miri et al. / Konda et al. |
| Energy consumption | Miri et al. |
| Model-selection methodology | Adel & Hassan |
| Real-world EV data | Caban et al. |
| OBD/CAN-style data analytics | Caban et al. |
| Digital-twin data connection | Caban et al. / Li et al. |
| Thermal modeling | Konda et al. |
| Validation methodology | Miri et al. / Konda et al. |

---

# Planned Literature-to-Development Workflow

The literature will be used approximately in the following order:

```text
Modeling Literature Review
        ↓
Define EV Powertrain Architecture
        ↓
Develop Longitudinal Vehicle Model
        ↓
Develop Motor / Inverter / Transmission Models
        ↓
Develop Battery and SOC Model
        ↓
Implement Regenerative Braking
        ↓
Run Drive-Cycle Simulation
        ↓
Energy Analytics
        ↓
Model Validation
        ↓
Real-World Data Interface
        ↓
Visualization / Dashboard
        ↓
Digital-Twin Pilot
