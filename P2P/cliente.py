from socket import *
from parametros import *
import sys
import binascii
import json


client_socket = socket(AF_INET, SOCK_DGRAM)

#criar mensagem modelo json
data = { "nome": "Luis",
		 "idade": "23",
		 "peso": "63"
		}
client_socket.sendto( json.dumps(data), adress)
resposta, addr = client_socket.recvfrom(102433)
resposta = json.loads(resposta)

print resposta