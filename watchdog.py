#!/usr/bin/env python

#https://forum.armbian.com/topic/2898-how-to-install-enable-and-start-watchdog-in-h3/
import time
import fcntl
f=open('/dev/watchdog','w')
try:
  while True:
    time.sleep(1)
    print '.'
    fcntl.ioctl(f,0x80045705) #WDIOC_KEEPALIVE

except KeyboardInterrupt:
    print 'end'
    f.write('V')
    f.close()

