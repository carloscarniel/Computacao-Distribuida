from socket import *
import sys
import binascii

adress=("localhost", 6005)
client_socket = socket(AF_INET, SOCK_DGRAM)

client_socket.sendto( "cheguei no servidor", adress)

resposta, addr = client_socket.recvfrom(11111)

print resposta