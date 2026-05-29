#!/usr/bin/env python3
# Traffic Light Detector - Main Node
# Author: Mohamed Hajjaj - The Inventor Hero
# GitHub: https://github.com/hajjajmohamed

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class TrafficLightDetector(Node):
    def __init__(self):
        super().__init__('traffic_light_detector')
        self.bridge = CvBridge()
        self.publisher = self.create_publisher(String, '/traffic_light/status', 10)
        self.image_sub = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.current_state = "UNKNOWN"
        self.get_logger().info('Traffic Light Detector Node Started')

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        state = self.detect_traffic_light(frame)
        if state != self.current_state:
            self.current_state = state
            result = String()
            result.data = state
            self.publisher.publish(result)
            self.get_logger().info(f'Traffic Light: {state}')

    def detect_traffic_light(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red detection
        red_low1  = np.array([0,   120, 70])
        red_high1 = np.array([10,  255, 255])
        red_low2  = np.array([170, 120, 70])
        red_high2 = np.array([180, 255, 255])
        red_mask  = cv2.inRange(hsv, red_low1, red_high1) +                     cv2.inRange(hsv, red_low2, red_high2)

        # Yellow detection
        yellow_low  = np.array([20, 100, 100])
        yellow_high = np.array([35, 255, 255])
        yellow_mask = cv2.inRange(hsv, yellow_low, yellow_high)

        # Green detection
        green_low  = np.array([40, 70, 70])
        green_high = np.array([90, 255, 255])
        green_mask = cv2.inRange(hsv, green_low, green_high)

        red_count    = cv2.countNonZero(red_mask)
        yellow_count = cv2.countNonZero(yellow_mask)
        green_count  = cv2.countNonZero(green_mask)

        threshold = 500
        if red_count > threshold and red_count >= yellow_count and red_count >= green_count:
            return "RED"
        elif yellow_count > threshold and yellow_count >= red_count and yellow_count >= green_count:
            return "YELLOW"
        elif green_count > threshold and green_count >= red_count and green_count >= yellow_count:
            return "GREEN"
        return "UNKNOWN"


def main(args=None):
    rclpy.init(args=args)
    node = TrafficLightDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
