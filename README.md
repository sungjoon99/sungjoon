# sungjoon
2023_02_13 ~ 2023_02_17 --> ROS2 특강
1day 8h --> 40h

---

## 2023_02_13


* 1교시
  * turtlebot3
  * VMware 17 Ubuntu 20.04

* 2교시
  * ROS2 DDS explain 미드웨어(DDS 전체)
  * commit / push / pull

* 3교시

  ```shell
  ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z :0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}'

  ros2 run turtlesim turtlesim_node

  ros2 run turtlesim turtle_teleop_key

  ```

  * ctrl + shift c/v/o/s 복사/붙여넣기/터미널새로만들기/글자크기조정

## 2023_2_14

- - -

* 1교시
  * 파이썬
   -자동 완성 기능
   -속도가 빠름
   -컴파일 없음

* 2교시
  * Package 만들기, 불러오기
  * Vscord를 활용한 파이썬

* 3교시
  *
