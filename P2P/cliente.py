from socket import *
from parametros import *
import sys
import binascii
import json
import funcoes

client_socket = socket(AF_INET, SOCK_DGRAM)

arquivoFinal= "testando.rar"
f=open(arquivoFinal, "wb")
for i in range(0, 40):
	data = { "tag": "DownloadRequest",
			 "nome": "teste.rar",
			 "numero_parte": i
			}
	print i		
	client_socket.sendto( json.dumps(data), adress)
	resposta, addr = client_socket.recvfrom(22222)
	resposta = json.loads(resposta)
	f.write(binascii.a2b_base64(resposta['part']))
f.close()
#print resposta