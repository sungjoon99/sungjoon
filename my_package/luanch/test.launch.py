from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_descriptiom():
  return LaunchDescription(
    Node(
      package='my_package',
    executable='moveturtle',
    name='move_turtle')
  )

