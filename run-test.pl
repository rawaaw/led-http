while (1){
  `curl -d "green=off&red=off" http://192.168.1.100`;
  sleep(1);
  `curl -d "green=off&red=on" http://192.168.1.100`;
  sleep(1);
  `curl -d "green=on&red=off" http://192.168.1.100`;
  sleep(1);
  `curl -d "green=on&red=on" http://192.168.1.100`;
  sleep(1);
}