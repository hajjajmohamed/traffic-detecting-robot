#!/usr/bin/env python3
# Standalone Test - No ROS2 needed
# Author: Mohamed Hajjaj - The Inventor Hero
# Run this to test detection with your webcam directly

import cv2
import numpy as np

def detect_traffic_light(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, np.array([0, 120, 70]),   np.array([10,  255, 255])) +                cv2.inRange(hsv, np.array([170, 120, 70]), np.array([180, 255, 255]))
    yellow_mask = cv2.inRange(hsv, np.array([20, 100, 100]), np.array([35, 255, 255]))
    green_mask  = cv2.inRange(hsv, np.array([40,  70,  70]), np.array([90, 255, 255]))

    r = cv2.countNonZero(red_mask)
    y = cv2.countNonZero(yellow_mask)
    g = cv2.countNonZero(green_mask)

    if max(r, y, g) < 500:
        return "UNKNOWN", (128, 128, 128)
    if r >= y and r >= g:
        return "RED",    (0, 0, 255)
    if y >= r and y >= g:
        return "YELLOW", (0, 255, 255)
    return "GREEN", (0, 255, 0)

cap = cv2.VideoCapture(0)
print("Traffic Light Detector - The Inventor Hero")
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    state, color = detect_traffic_light(frame)
    cv2.rectangle(frame, (10, 10), (300, 60), color, -1)
    cv2.putText(frame, f'Light: {state}',
                (20, 45), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 255, 255), 2)
    cv2.circle(frame, (580, 40), 30, color, -1)
    cv2.imshow('Traffic Detector - Standalone Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
