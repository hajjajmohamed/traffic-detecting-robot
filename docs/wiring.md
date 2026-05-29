# Wiring Guide - Traffic Detecting Robot

## Camera Module -> Raspberry Pi 4

| Camera    | RPi          |
|-----------|--------------|
| USB Camera| USB Port     |
| Pi Camera | CSI Port     |

## Motor Driver L298N -> Raspberry Pi 4

| L298N | RPi GPIO |
|-------|----------|
| IN1   | GPIO 17  |
| IN2   | GPIO 18  |
| IN3   | GPIO 22  |
| IN4   | GPIO 23  |
| ENA   | GPIO 24  |
| ENB   | GPIO 25  |
| GND   | GND      |
| VCC   | 5V       |

## OLED SSD1306 -> Raspberry Pi 4

| OLED | RPi    |
|------|--------|
| VCC  | 3.3V   |
| GND  | GND    |
| SCL  | GPIO 3 |
| SDA  | GPIO 2 |
