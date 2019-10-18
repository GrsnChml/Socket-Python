import socket 
  
UDP_IP = "3.15.164.75"
UDP_PORT = 50012
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) ;
​
​
def stripped(s):
    return "".join(i for i in s if 31 < ord(i) < 127)
​
  
while True: 
    data, addr = sock.recvfrom(1024);
    data = stripped(data.decode('utf-8')).strip()
    data1 = data.split(',')
    print ("TIPO: ", data1[1]);
    print ("IMEI: ", data1[2]);
    print ("LONGITUD: ", data1[11]);
    print ("LATITUD: ", data1[12]);
    print ("HORA/FECHA: ", data1[13]);
    print ("VELOCIDAD: ", data1[19]);
    print ("", data1);
    break;