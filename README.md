# Intelligent Traffic-Detecting Robot

AI-powered robot that detects traffic lights and road signals using OpenCV and ROS2.

## Features
- Real-time traffic light detection (Red / Yellow / Green)
- HSV color space analysis for accurate detection
- ROS2 node architecture for modular control
- Autonomous stop/go behavior based on light state
- Live visual overlay with detection status
- Standalone test mode (no ROS2 required)

## Tech Stack

| Category  | Technologies              |
|-----------|---------------------------|
| Vision    | OpenCV, NumPy             |
| Framework | ROS2 Humble               |
| Language  | Python 3                  |
| Hardware  | Raspberry Pi 4, USB Camera|
| OS        | Ubuntu 22.04              |

## Project Structure

    traffic-detecting-robot/
    src/
        traffic_detector.py    - HSV color detection node
        robot_controller.py    - Motor control based on light
        camera_node.py         - Camera capture node
        visualizer.py          - Live visual overlay
        standalone_test.py     - Test without ROS2
    docs/
        wiring.md              - Hardware wiring guide
    media/                     - Photos and demo videos
    requirements.txt

## Installation

    git clone https://github.com/hajjajmohamed/traffic-detecting-robot.git
    cd traffic-detecting-robot
    pip install -r requirements.txt

## Usage

### Standalone test (no ROS2 needed)
    python3 src/standalone_test.py

### Full ROS2 mode
    source /opt/ros/humble/setup.bash
    python3 src/camera_node.py
    python3 src/traffic_detector.py
    python3 src/robot_controller.py
    python3 src/visualizer.py

## How It Works
1. Camera captures live frames
2. HSV color analysis detects light color
3. Robot reacts: RED=stop, YELLOW=slow, GREEN=go
4. Visual overlay shows detection result in real time

## Author
Mohamed Hajjaj - The Inventor Hero
National Innovation Champion 2026
GITEX Africa 2026 Participant
GitHub: https://github.com/hajjajmohamed
Instagram: https://instagram.com/the.inventor.hero
