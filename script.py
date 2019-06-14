import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('xxx.xxx.xxx.xxx', xxxx))
client_socket.settimeout(10)

time.sleep(2)
string = "status 1" + '\r\n'
arr = bytes(string, 'utf-8')
client_socket.send(arr)

GPS_List = [0.0]

while True:

	data = client_socket.recv(1024)
	if data == "":
		break
	GPS_List = data.split()

	print (GPS_List[1])
	#Solution = GPS_List[40]
	#print (Solution)
	#x = 1
	#for str in GPS_List:
	#	print ("%s %s") % (x, str)
	#	x += 1



	time.sleep(1)
