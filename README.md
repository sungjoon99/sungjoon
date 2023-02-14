# sungjoon
첫 커밋

---

## 2023_02_13

---

* 1교시
  * turtlebot3
  * VMware 17 Ubuntu 20.04

* 2교시
  * ROS2 DDS explain

* t3교시

```shell
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z :0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}'

ros2 run turtlesim turtlesim_node

ros2 run turtlesim turtle_teleop_key

```
