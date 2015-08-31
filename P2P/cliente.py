from socket import *
from parametros import *
import sys
import binascii
import json
import funcoes


hashDoArquivoTeste1="c421622366dd30b5dfc83eed1e1b759139560b21bcc43e03ff21f8aa3aba4c45"


arquivo1="teste.rar"
arquivoFinal= "testando.rar"


client_socket = socket(AF_INET, SOCK_DGRAM)


f=open(arquivoFinal, "wb")
for i in range(0, 33):
	data = { "tag": "DownloadRequest",
			 "hash": hashDoArquivoTeste1,
			 "numero_parte": i
			}
	print i		
	client_socket.sendto( json.dumps(data), adress)
	resposta, addr = client_socket.recvfrom(102400)
	resposta = json.loads(resposta)
	f.write(binascii.a2b_base64(resposta['parte']))
	print data
f.close()
if funcoes.hashDoArquivo(arquivo1) == funcoes.hashDoArquivo(arquivoFinal):
	print 'Arquivo transferido e verificdo com sucesso'

