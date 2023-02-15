# sungjoon
2023_02_13 ~ 2023_02_17 --> ROS2 특강
1day 8h --> 40h
* 사용교재
  -https://freshmea.notion.site/freshmea/ROS2-5a5303ac2160454885498a52dfce26c4#dd0cb4d7b7524df2bcee959032195367

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

  * cw --> cd ~/robot_ws
  * cs --> cd ~/robot_ws/src
  * sb --> source ~/.bashrc 재부팅
  * cb --> colcon build 변경사항 업데이트

- - -

## 2023_02_15

* 1교시

  * launch 파일 생성
  * ros2 launch my_package test2.launch.py

* 2교시

 * STM32 - Esp32 칩이름
 * Micro-Ros (setup,loop)
 * 마블링크
 * 라즈베리파이와 Open CR 둘 다 사용하는 이유
  -Open CR이 잔업을 분업하여 라즈베리파이가 Real-Time(실시간통신) 가능

* 3교시

  * IMU
    -6축(사용)
      -자이로센서 3축
      -가속도센서 3축
    -9축

  * Ubuntu 서버 장점
    -빠르고 작다
    -Test

  * 로보티즈 사이트를 통해 터틀봇 연결

    -SD카드에 Ubuntu 다운받고 와이파이 동일화 터틀봇에 SD카드 삽입

  * 통신
    -라즈베리파이와 IMU 전원선(5v) 연결하여 Topic Data통신함
      --> 라즈베리파이와 IMU 데이터 형식을 Micro-Ros를 통해 변환하여 Topic 통신함

  * Open CR Setup
    -https://emanual.robotis.com/docs/en/platform/turtlebot3/opencr_setup/#opencr-setup

  * 터틀봇 조작

    * PC Setup(6-1-2)

    * SBC Setup
      -https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup

    * Turtlebot3 키보드 조작

    turtlebot3 모델 정의
    재부팅
    키보드 조작

    '''

    export TURTLEBOT3_MODEL=burger
    source .bashrc
    ros2 launch turtlebot3_bringup robot.launch.py

    ros2 run turtlebot3_teleop teleop_keyboard

    '''
