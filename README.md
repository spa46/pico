# 🌱 Raspberry Pi Pico Hydroponics System

## 1️⃣ Required Components

### 🖥️ Microcontroller

- **Raspberry Pi Pico** (MicroPython Compatible)

### 🌡️ Sensors

- **DHT22** – Temperature & Humidity Sensor
- **MH-Z19B** – CO2 Sensor (UART Communication)
- **Industrial pH Sensor** – Measures pH level of the nutrient solution
- **EC Sensor** – Measures electrical conductivity (nutrient concentration)
- **Water Level Sensor** – Detects if water level is low

### ⚙️ Actuators

- **Water Pump** – Circulates water in the hydroponics system
- **Solenoid Valve** – Adjusts pH by adding alkaline or acidic solutions
- **LED Grow Lights** – Provides artificial lighting for plant growth
- **Cooling Fan** – Helps regulate temperature in the system

### 📟 Display

- **16x2 I2C LCD Display** – Shows sensor readings & system status

---

## 2️⃣ Interfaces & Connections

### 🎛️ **Analog Inputs (ADC)**

| Component            | Pico Pin    |
| -------------------- | ----------- |
| Industrial pH Sensor | GP26 (ADC0) |
| EC Sensor            | GP27 (ADC1) |

### 📡 **Digital Inputs**

| Component               | Pico Pin |
| ----------------------- | -------- |
| DHT22 (Temp & Humidity) | GP3      |
| Water Level Sensor      | GP4      |

### 🔗 **UART Communication**

| Component            | TX Pin | RX Pin | Baud Rate |
| -------------------- | ------ | ------ | --------- |
| MH-Z19B (CO2 Sensor) | GP16   | GP17   | 9600      |

### 🔌 **Actuator Outputs**

| Component       | Pico Pin |
| --------------- | -------- |
| Water Pump      | GP10     |
| Solenoid Valve  | GP12     |
| LED Grow Lights | GP13     |
| Cooling Fan     | GP14     |

### 📟 **I2C Communication (for LCD Display)**

| Signal | Pico Pin |
| ------ | -------- |
| SDA    | GP20     |
| SCL    | GP21     |

---

## 2 Run
There are two ways to run the project.
1. Emulator
2. Target Board


### 2.1 Run on Emulator


To run the project with Emulator, follow the steps below.
_**Renode**_ is used for the emulation.

git submodule update --init --recursive

```
docker run -ti -e DISPLAY -v $XAUTHORITY:/home/developer/.Xauthority --net=host antmicro/renode:1.15.2
docker run -ti -e DISPLAY -v $XAUTHORITY:/home/developer/.Xauthority -v renode_rp2040:/opt/renode/rp2040 --net=host antmicro/renode:1.15.2
```