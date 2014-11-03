import socket
import time 

UDP_PORT = 1078 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.1.107", UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	reception_time = time.time() 
	print reception_time
	print "received message:", data 
	arr = data.split()
	reply = "{} {} {:.6f} {:.6f}".format(arr[0],arr[1],reception_time,time.time())
	sock.sendto(reply, addr) 
	
