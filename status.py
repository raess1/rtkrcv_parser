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
          key = '# of satellites rover'
          key = '# of satellites base'
          key = '# of valid satellites'
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
             #print('sats rover:'+dict['# of satellites rover'])
             #print('solution status:'+dict['solution status'])

             
             #Split GDOP/PDOP/HDOP/VDOP in to diffrent parameters#
             GPHV = dict['GDOP/PDOP/HDOP/VDOP']
             #print (GPHV)
             GPHV_Split = GPHV.split(",")
             #print (GPHV_Split[0])
             #print (GPHV_Split[1])
             #print (GPHV_Split[2])
             #print (GPHV_Split[3])
             GDOP = GPHV_Split[0]
             PDOP = GPHV_Split[1]
             HDOP = GPHV_Split[2]
             PDOP = GPHV_Split[3]
             #print (GDOP)

             #pos xyz single (m) rover in to diffrent parameters#
             POS_Single = dict['pos xyz single (m) rover']
             #print (POS_Single)
             POS_Single_Split = POS_Single.split(",")
             POS_Single_X = POS_Single_Split[0]
             POS_Single_Y = POS_Single_Split[1]
             POS_Single_Z = POS_Single_Split[2]
             #print (POS_Single_X)
             #print (POS_Single_Y)
             #print (POS_Single_Z)

             #vel enu (m/s) rover #
             VEL_Enu = dict['vel enu (m/s) rover']
             VEL_Enu_Split = VEL_Enu.split(",")
             #print (VEL_Enu_Split)
             VEL_Enu_X = VEL_Enu_Split[0]
             VEL_Enu_Y = VEL_Enu_Split[1]
             VEL_Enu_Z = VEL_Enu_Split[2]
             #print (VEL_Enu_X)
             #print (VEL_Enu_Y)
             #print (VEL_Enu_Z)

             #pos xyz float in to diffrent parameters#
             POS_XYZ_Float = dict['pos xyz float (m) rover']
             POS_XYZ_Float_Split = POS_XYZ_Float.split(",")
             #print (POS_XYZ_Float_Split)
             POS_XYZ_Float_X = POS_XYZ_Float_Split[0]
             POS_XYZ_Float_Y = POS_XYZ_Float_Split[1]
             POS_XYZ_Float_Z = POS_XYZ_Float_Split[2]
             #print (POS_XYZ_Float_X)
             #print (POS_XYZ_Float_Y)
             #print (POS_XYZ_Float_Z)

             #pos xyz float std (m) rover in to diffrent parameters#
             POS_XYZ_Float_Std = dict['pos xyz float std (m) rover']
             POS_XYZ_Float_Std_Split = POS_XYZ_Float_Std.split(",")
             #print (POS_XYZ_Float_Std_Split)
             POS_XYZ_Float_Std_X = POS_XYZ_Float_Std_Split[0]
             POS_XYZ_Float_Std_Y = POS_XYZ_Float_Std_Split[1]
             POS_XYZ_Float_Std_Z = POS_XYZ_Float_Std_Split[2]
             #print (POS_XYZ_Float_Std_X)
             #print (POS_XYZ_Float_Std_Y)
             #print (POS_XYZ_Float_Std_Z)


             #pos xyz fixed (m) rover in to diffrent parameters#
             POS_XYZ_Fixed = dict['pos xyz fixed (m) rover']
             POS_XYZ_Fixed_Split = POS_XYZ_Fixed.split(",")
             #print (POS_XYZ_Fixed_Split)
             POS_XYZ_Fixed_X = POS_XYZ_Fixed_Split[0]
             POS_XYZ_Fixed_Y = POS_XYZ_Fixed_Split[1]
             POS_XYZ_Fixed_Z = POS_XYZ_Fixed_Split[2]
             #print (POS_XYZ_Fixed_X)
             #print (POS_XYZ_Fixed_Y)
             #print (POS_XYZ_Fixed_Z)


             #pos xyz fixed (m) rover in to diffrent parameters#
             POS_XYZ_Fixed_Std = dict['pos xyz fixed std (m) rover']
             POS_XYZ_Fixed_Std_Split = POS_XYZ_Fixed_Std.split(",")
             #print (POS_XYZ_Fixed_Std_Split)
             POS_XYZ_Fixed_Std_X = POS_XYZ_Fixed_Std_Split[0]
             POS_XYZ_Fixed_Std_Y = POS_XYZ_Fixed_Std_Split[1]
             POS_XYZ_Fixed_Std_Z = POS_XYZ_Fixed_Std_Split[2]
             #print (POS_XYZ_Fixed_Std_X)
             #print (POS_XYZ_Fixed_Std_Y)
             #print (POS_XYZ_Fixed_Std_Z)

             #pos xyz (m) base in to diffrent parameters#
             POS_XYZ_Base = dict['pos xyz (m) base']
             POS_XYZ_Base_Split = POS_XYZ_Base.split(",")
             #print (POS_XYZ_Fixed_Std_Split)
             POS_XYZ_Base_X = POS_XYZ_Base_Split[0]
             POS_XYZ_Base_Y = POS_XYZ_Base_Split[1]
             POS_XYZ_Base_Z = POS_XYZ_Base_Split[2]
             print (POS_XYZ_Base_X)
             print (POS_XYZ_Base_Y)
             print (POS_XYZ_Base_Z)


             #pos llh (deg,m) base in to diffrent parameters#
             POS_LLH_Base = dict['pos llh (deg,m) base']
             POS_LLH_Base_Split = POS_LLH_Base.split(",")
             #print (POS_XYZ_Fixed_Std_Split)
             POS_LLH_Base_Latitude = POS_LLH_Base_Split[0]
             POS_LLH_Base_Longitude = POS_LLH_Base_Split[1]
             POS_LLH_Base_Height = POS_LLH_Base_Split[2]
             #print (POS_LLH_Base_Latitude)
             #print (POS_LLH_Base_Longitude)
             #print (POS_LLH_Base_Height)
