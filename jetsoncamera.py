cd Downloads

git clone  https://github.com/jetsonworld/jetson-fan-ctl.git

ls

cd jetson-fan-ctl

sudo sh install.sh

sudo apt-get upgrade

sudo apt-get update

sudo apt install python3-pip
(설치해야 스크린 캡쳐기능 실행 가능)

sudo pip3 list

sudo -H pip3 install -U jetson-stats

pip3 list| grep jetson
(jetson-stats & 버전 / 대충 이렇게 뜨면 리부트)

reboot rc@rc-desktop:~$ reboot 

rc@rc-desktop:~$ jtop
(실행하면 제슨 나노 상테 확인 가능)

ifconfig
(제슨 나노 아이피 확인)

ls /dev/video0 -l
(제슨이 카메라 인식을 하는 지 확인하는지 확인하는 명령어)

git clone https://github.com/jetsonhacks/USB-Camera.git

ls

cd USB-Camera

ls
(요거 실행하면 face-detect-usb.py  LICENSE  README.md  usb-camera-gst.py  usb-camera-simple.py 이거 세가지가 뜸)

python3 usb-camera-gst.py 
(실행하면 카메라 켜짐)
