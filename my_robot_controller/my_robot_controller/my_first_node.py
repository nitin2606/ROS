import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("ROS")
        self.create_timer(1.0, self.timer_callback)  # this will execute timer_callback every 1 sec

    def timer_callback(self):
        self.get_logger().info("Hello")
        

def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)  # Keeps the node alive
    
    rclpy.shutdown()


if __name__ == '__main__':
    main()