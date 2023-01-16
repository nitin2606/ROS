import rclpy
from rclpy import Node
from geometry_msgs.msg import Twist


class DrawSquare(Node):

    def __init__(self):
        super().__init__("draw_square")
        self.cmd_vel_pub = self.create_publisher
