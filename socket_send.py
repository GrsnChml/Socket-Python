import socket
import time
import random
​
UDP_IP = "3.15.164.75"
UDP_PORT = 50012
MESSAGE = "$GPRMC,222222.22,A,0328.438806,N,07631.607717,W,0.0,0.0,190714,3.8,E,A*2B"
 
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
 
i = 0
while i < 50: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto((MESSAGE + str(i)).encode('utf-8'), (UDP_IP, UDP_PORT))
    a = random.randrange(1);
    time.sleep(a)
    i += 1
    print (i)