import socket
import time
import random
UDP_IP = "192.168.0.105"
UDP_PORT = 50012
MESSAGE = "+RESP:GTFRI,500100,864802030229557,,,10,1,5,0.0,0,512.1,-89.421421,16.333872,20191003173607,0704,0002,756E,BBA9E71,00,0.0,,,,0,110000,,,,20191003173611,0604$"
 
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
 
i = 0
while i < 1: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto((MESSAGE + str(i)).encode('utf-8'), (UDP_IP, UDP_PORT))
    a = random.randrange(1);
    time.sleep(a)
    i += 1
    print (i)