# importing socket module 
import socket 
import MySQLdb
  
conn = MySQLdb.connect(host= "spaceapp.ch7oeqwewnpa.us-west-2.rds.amazonaws.com",
                  user="admin",
                  passwd="1234abcd",
                  db="robot_db")

x = conn.cursor()   

UDP_IP = "3.15.164.75"
UDP_PORT = 50012
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 


def stripped(s):
    return "".join(i for i in s if 31 < ord(i) < 127)

def sendDataToDataBase(longitud,latitud,velocidad):
    try:
        x.execute("""INSERT INTO trama VALUES (null,'%s','%s','%s',Now())""",(latitud,longitud,velocidad));
        print("success");
        conn.commit();
    except:
        conn.rollback();
        print("error");

  
while True: 
    data, addr = sock.recvfrom(1024);
    data = stripped(data.decode('utf-8')).strip()
    data1 = data.split(',')
    sendDataToDataBase(data1[11],data1[12],data1[19]);
    print ("", data1);
    break;


conn.close();