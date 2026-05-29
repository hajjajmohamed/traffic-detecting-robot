#!/usr/bin/env python3
# Traffic Light Visualizer - Shows detection result on screen
# Author: Mohamed Hajjaj - The Inventor Hero

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

STATE_COLORS = {
    "RED":     (0,   0,   255),
    "YELLOW":  (0,   255, 255),
    "GREEN":   (0,   255, 0),
    "UNKNOWN": (128, 128, 128)
}

class Visualizer(Node):
    def __init__(self):
        super().__init__('visualizer')
        self.bridge = CvBridge()
        self.state = "UNKNOWN"
        self.create_subscription(String, '/traffic_light/status', self.state_cb, 10)
        self.create_subscription(Image,  '/camera/image_raw',     self.frame_cb, 10)
        self.get_logger().info('Visualizer Node Started')

    def state_cb(self, msg):
        self.state = msg.data

    def frame_cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        color = STATE_COLORS.get(self.state, (128, 128, 128))

        # Draw status box
        cv2.rectangle(frame, (10, 10), (300, 60), color, -1)
        cv2.putText(frame, f'Traffic: {self.state}',
                    (20, 45), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (255, 255, 255), 2)

        # Draw circle indicator
        cv2.circle(frame, (580, 40), 30, color, -1)
        cv2.imshow('Traffic Light Detector - The Inventor Hero', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = Visualizer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
