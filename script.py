import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('000.000.000.000', 5000))
client_socket.settimeout(10)
GPS_List = [0.0]
time.sleep(2)


string = "status 1" + '\r\n'
client_socket.send("status 1" + '\r\n')



dict = {}

while True:

        data = client_socket.recv(1024)
        lines = data.split("\n")
        for line in lines:
          #print(line)
          cols = line.split(":")          
          if len(cols) >= 2:
            dict[cols[0].strip()] = cols[1].strip()
            #print(cols[0])          
          key = 'rtklib version'
          key = 'rtk server thread'
          key = 'rtk server state'
          key = 'processing cycle (ms)'
          key = 'positioning mode'
          key = 'frequencies'
          key = 'accumulated time to run'
          key = 'cpu time for a cycle (ms)'
          key = 'missing obs data count'
          key = 'bytes in input buffer'
          key = '# of input data rover'
          key = '# of input data base'
          key = '# of input data corr'
          key = '# of rtcm messages rover'
          key = '# of rtcm messages base'
          key = '# of rtcm messages corr'
          key = 'solution status'
          key = 'time of receiver clock rover'
          key = 'time sys offset (ns)'
          key = 'solution interval (s)'
          key = 'age of differential (s)'
          key = 'ratio for ar validation'
          key = 'GDOP/PDOP/HDOP/VDOP'
          key = '# of real estimated states'
          key = '# of all estimated states'
          key = 'pos xyz single (m) rover'
          key = 'pos llh single (deg,m) rover'
          key = 'vel enu (m/s) rover'
          key = 'pos xyz float (m) rover'
          key = 'pos xyz float std (m) rover'
          key = 'pos xyz fixed (m) rover'
          key = 'pos xyz fixed std (m) rover'
          key = 'pos xyz (m) base'
          key = 'pos llh (deg,m) base'
          key = '# of average single pos base'
          key = 'ant type rover'
          key = 'ant delta rover'
          key = 'ant delta base'
          key = 'vel enu (m/s) base'
          key = 'baseline length float (m)'
          key = 'baseline length fixed (m)'
          key = 'last time mark'
          key = 'receiver time mark count'
          key = 'rtklib time mark count'
          if key in dict:
             print('sats rover:'+dict[key])                    
        
        #for key in dict:
        #  print('KEY='+key+'  VALUE='+dict[key])
        
        time.sleep(0.1)
        #print(dict)


