#aplicação servidora utilizando protocolo udp

from socket import *
import time


server = 'localhost'
door = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)

obj_socket.bind((server, door))
print("Server ready!")
time.sleep(5)
print("Waiting for conection...")

while True:
	data, origin = obj_socket.recvfrom(65535)
	print("Origin.........: ", origin)
	print("Received data..: ", data)
	answer = input("Type the answer: ")
	obj_socket.sendto(answer.encode(), origin)

obj_socket.close()