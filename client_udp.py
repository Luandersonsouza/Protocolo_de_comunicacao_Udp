#aolicação cliente seguindo o protocolo UDP!
import time
from socket import *

server = 'localhost'
door = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, door))
output =""
print("Successfully connected!")

while output != "X":
	message = input("Type something: ")
	obj_socket.sendto(message.encode(), (server, door))
	data, origin = obj_socket.recvfrom(65535)
	print("Server response: ", data.decode())
	time.sleep(5)
	output = input ("Type <X> to exit: ").upper()

obj_socket.close()