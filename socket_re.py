# importing socket module 
import socket 
import MySQLdb
import datetime 
import pytz 

# TODO: no exponer datos de cuentas y conexiones, ya que es un repositorio publico.
db_host = "spaceapp.ch7oeqwewnpa.us-west-2.rds.amazonaws.com"
db_user = "admin"
db_password = "1234abcd"
db_database = "robot_db"

UDP_IP = "192.168.0.105"
UDP_PORT = 50012

conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_database)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 
x = conn.cursor()

def stripped(s):
    return "".join(i for i in s if 31 < ord(i) < 127)


def sendDataToDataBase(longitud,latitud,velocidad):
    try:
        current_time = datetime.datetime.now(pytz.timezone('America/Guatemala')) 
        
        x.execute("""INSERT INTO trama VALUES (null,%s,%s,%s,%s)""",(latitud,longitud,velocidad,current_time));
        print("success");
        conn.commit();
        
    except Exception as error:
        conn.rollback();
        print("error " + error);
        

  
while True: 
    data, addr = sock.recvfrom(1024);
    data = stripped(data.decode('utf-8')).strip()
    data1 = data.split(',')
    if data1[11] and data1[12] and data1[19]:
        sendDataToDataBase(data1[11],data1[12],data1[19]);

