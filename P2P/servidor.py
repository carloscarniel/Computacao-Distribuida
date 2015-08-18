from socket import *
import binascii
import sys

adress=("localhost", 6005)
server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(adress)
requisicao, addr = server_socket.recvfrom(1024)


while(1):
	print requisicao
	server_socket.sendto("cheguei no cliente", addr)