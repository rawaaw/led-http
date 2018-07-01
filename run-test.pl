while (1){
  `curl -m 10 -d "green=off&red=off" http://192.168.1.100`;
  sleep(1);
  `curl -m 10 -d "green=off&red=on" http://192.168.1.100`;
  sleep(1);
  `curl -m 10 -d "green=on&red=off" http://192.168.1.100`;
  sleep(1);
  `curl -m 10 -d "green=on&red=on" http://192.168.1.100`;
  sleep(1);
}