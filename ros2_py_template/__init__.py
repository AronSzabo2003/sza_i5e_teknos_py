import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class HeartDraw(Node):
    def __init__(self):
        super().__init__('heart_draw')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.count_ = 0
        self.get_logger().info("Drawing a heart shape in turtlesim.")
        self.loop()

    def publish_message(self, fwd, turn, duration=2):
        message = Twist()
        message.linear.x = fwd
        message.angular.z = turn
        self.count_ += 1
        self.get_logger().info(f"Step {self.count_}. speed: {message.linear.x:.1f} turn: {message.angular.z:.1f}")
        self.publisher_.publish(message)
        time.sleep(duration)  # Delay for specified duration

    def loop(self):
        self.get_logger().info("Loop started.")
        time.sleep(2)  # Initial delay

        # Drawing heart shape path
        self.publish_message(2.0, math.pi / 4, 1.5)  # Curve up right
        self.publish_message(0.0, -math.pi / 2, 1.0)  # Rotate left
        self.publish_message(2.0, -math.pi / 4, 1.5)  # Curve down left
        self.publish_message(2.0, math.pi / 4, 1.5)  # Curve up left
        self.publish_message(0.0, -math.pi / 2, 1.0)  # Rotate left
        self.publish_message(2.0, -math.pi / 4, 1.5)  # Curve down right
        self.publish_message(2.0, 0.0, 2.0)  # Move to close the heart

        self.get_logger().info("Program finished")
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = HeartDraw()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
