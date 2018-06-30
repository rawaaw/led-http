apt-get update
apt install python-pip
apt install python3-pip

pip install --upgrade OPi.GPIO
#pip3 install --upgrade OPi.GPIO

apt-get install watchdog

python http.py

curl -d "green=off&red=off" http://192.168.1.100
curl -d "green=on&red=off" http://192.168.1.100
