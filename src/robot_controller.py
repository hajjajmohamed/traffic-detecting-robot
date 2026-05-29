#!/usr/bin/env python3
# Robot Controller - Reacts to traffic light state
# Author: Mohamed Hajjaj - The Inventor Hero

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

SPEED_NORMAL = 0.3
SPEED_SLOW   = 0.1

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.create_subscription(String, '/traffic_light/status', self.light_callback, 10)
        self.get_logger().info('Robot Controller Node Started')

    def light_callback(self, msg):
        state = msg.data
        twist = Twist()

        if state == "RED":
            self.get_logger().warn('RED light - STOP')
            twist.linear.x = 0.0

        elif state == "YELLOW":
            self.get_logger().warn('YELLOW light - Slowing down')
            twist.linear.x = SPEED_SLOW

        elif state == "GREEN":
            self.get_logger().info('GREEN light - Moving forward')
            twist.linear.x = SPEED_NORMAL

        else:
            self.get_logger().info('Unknown state - Stopping')
            twist.linear.x = 0.0

        self.cmd_pub.publish(twist)

    def stop(self):
        self.cmd_pub.publish(Twist())


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.stop()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
