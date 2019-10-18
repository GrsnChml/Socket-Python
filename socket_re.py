# importing socket module 
import socket 
import MySQLdb
import datetime 
import pytz 

  
conn = MySQLdb.connect(host= "spaceapp.ch7oeqwewnpa.us-west-2.rds.amazonaws.com",
                  user="admin",
                  passwd="1234abcd",
                  db="robot_db")

   
current_time = datetime.datetime.now(pytz.timezone('America/Guatemala')) 


UDP_IP = "192.241.219.11"
UDP_PORT = 50012
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 


def stripped(s):
    return "".join(i for i in s if 31 < ord(i) < 127)

def sendDataToDataBase(longitud,latitud,velocidad):
    try:
        x = conn.cursor()
        print(longitud)
        print(latitud)
        print(velocidad)
        x.execute("""INSERT INTO trama VALUES (null,%s,%s,%s,%s)""",(latitud,longitud,velocidad,current_time));
        print("success");
        conn.commit();
        conn.close();
    except Exception as error:
        conn.rollback();
        print("error " + error);
        conn.close();

  
while True: 
    data, addr = sock.recvfrom(1024);
    data = stripped(data.decode('utf-8')).strip()
    data1 = data.split(',')
    sendDataToDataBase(data1[11],data1[12],data1[19]);
    break;

