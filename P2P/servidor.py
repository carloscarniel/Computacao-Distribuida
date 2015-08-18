from socket import *
from parametros import *
import sys
import binascii



server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(adress)
requisicao, addr = server_socket.recvfrom(1024)


while(1):
	print requisicao
	server_socket.sendto("cheguei no cliente", addr)