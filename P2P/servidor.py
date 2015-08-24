from socket import *
from parametros import *
import sys
import binascii
import json
import funcoes

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(adress)

lista_de_arquivos=[]
lista_de_arquivos=funcoes.carregaArquivos(lista_de_arquivos)


while(1):

	print "escutando"
	requisicao, addr = server_socket.recvfrom(22222)
	requisicao = json.loads(requisicao)

	for i in lista_de_arquivos:
		if  i['nome'] == "teste.rar" and i['parte'] == requisicao['numero_parte'] :
			resposta ={"tag":"DownloadResponse",
			"tamanho_parte":len(i['data']),
			"numero_parte":i['parte'],
			"numero_de_partes":i['totalPartes'],
			"part": binascii.b2a_base64(i['data'])
			}

			server_socket.sendto(json.dumps(resposta), addr)