import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('000.000.000.000', 5000))
client_socket.settimeout(10)
GPS_List = [0.0]
time.sleep(2)
string = "status 1" + '\r\n'
client_socket.send("status 1" + '\r\n')


while True:

        data = client_socket.recv(1024)
        #print(data)
        #if data == "  ":
        #       break
        #GPS_List = data.split("'")

        #GPS_List2 = GPS_List.split()

        #print (GPS_List)
        lines = data.split("\n")
        for line in lines:
          #print(line)
          cols = line.split(":")          
          #print(cols[0])
          if (cols[0].strip() == '# of satellites rover'):
            print('sats rover:' + cols[1])
        #print (GPS_List[0])
        time.sleep(0.1)

