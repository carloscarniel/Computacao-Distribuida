from socket import *
from parametros import *
import sys
import binascii
import json


server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(adress)
requisicao, addr = server_socket.recvfrom(1024)
requisicao = json.loads(requisicao)

print requisicao

resposta ={"Peso":"ideal",
		"Altura":"ok"
		}


server_socket.sendto(json.dumps(resposta), addr)