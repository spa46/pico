# pico

## 1. Required Components

(A) Sensors
pH Sensor – Monitors the acidity/alkalinity of the nutrient solution.
EC (Electrical Conductivity) Sensor – Measures the concentration of dissolved salts.
Temperature Sensor (DS18B20) – Monitors water temperature.
Humidity & Air Temperature Sensor (DHT22) – Monitors ambient conditions.
Water Level Sensor – Ensures adequate water levels.
Light Sensor (BH1750 or LDR) – Measures light intensity.
CO2 Sensor (MH-Z19B) – Measures carbon dioxide levels.

B) Peripherals
Water Pump (Relay Module) – Circulates nutrient solution.
Air Pump (Relay Module) – Provides oxygenation.
Solenoid Valve (Relay Module) – Controls nutrient flow.
LED Grow Lights (MOSFET) – Provides artificial lighting.
Cooling Fan (MOSFET/Relay) – Controls temperature.
LCD/OLED Display (I2C SSD1306) – Displays system status.
Buzzer – Alerts on critical conditions.

## 2. Interfaces & Connections
| Sensor/Peripheral       | Interface | Pins Used (Example)     |
|-------------------------|-----------|-------------------------|
| pH Sensor              | Analog    | ADC0 (GP26)             |
| EC Sensor              | Analog    | ADC1 (GP27)             |
| DS18B20 (Water Temp)   | 1-Wire    | GP2                     |
| DHT22 (Air Temp & Humidity) | Digital  | GP3                     |
| Water Level Sensor     | Digital   | GP4                     |
| BH1750 (Light Sensor)  | I2C       | SDA (GP20), SCL (GP21)  |
| MH-Z19B (CO2 Sensor)   | UART      | TX(GP8), RX(GP9)        |
| Water Pump (Relay)     | Digital   | GP10                    |
| Air Pump (Relay)       | Digital   | GP11                    |
| Solenoid Valve (Relay) | Digital   | GP12                    |
| LED Grow Lights (MOSFET) | Digital | GP13                    |
| Cooling Fan (Relay)    | Digital   | GP14                    |
| OLED Display (SSD1306) | I2C       | SDA (GP20), SCL (GP21)  |
| Buzzer                | PWM       | GP15                    |
