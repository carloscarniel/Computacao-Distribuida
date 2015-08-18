from socket import *
from parametros import *
import sys
import binascii



client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.sendto( "cheguei no servidor", adress)
resposta, addr = client_socket.recvfrom(1024)

print resposta