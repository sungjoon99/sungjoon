import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class M_turtle(Node):
  def __init__(self):
    super().__init__('move_turtle')
    self.qos = QoSProfile(depth = 10)
    self.pub1 = self.create_publisher(Twist, 'turtle1/cmd_vel', self.qos)
    self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', self.qos)
    self.create_timer(0.1, self.pubmessage)
    self.vel = 0.0

  def pubmessage(self):
    msg = Twist()
    msg.linear.x = self.vel
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 2.5

    msg2 = Twist()
    msg2.linear.x = self.vel
    msg2.linear.y = 0.0
    msg2.linear.z = 0.0
    msg2.angular.x = 0.0
    msg2.angular.y = 0.0
    msg2.angular.z = 2.5

    self.pub.publish(msg)
    self.pub.publish(msg2)
    self.get_logger().info(f'Seding message: [{msg}]')
    self.vel += 0.04
    if self.vel > 3.0:
      self.vel = 0.0

def main():
  rclpy.init()
  node = M_turtle()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

