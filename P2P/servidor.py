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


#	teste=open('hashfinal.txt','wb')
#	juca=funcoes.hashDoArquivo("testando.rar")
#	teste.write(juca)
#	teste.close()

	print "escutando"
	requisicao, addr = server_socket.recvfrom(22222)
	requisicao = json.loads(requisicao)

	for i in lista_de_arquivos:
		if  i['hash_do_arquivo'] == requisicao['hash'] and i['parte'] == requisicao['numero_parte'] :
			resposta ={"tag":"DownloadResponse",
			"parte_hash":i['hash_da_parte'],
			"tamanho_parte":len(i['data']),
			"numero_parte":i['parte'],
			"numero_de_partes":i['totalPartes'],
			"parte": binascii.b2a_base64(i['data'])
			}

			print "parte_hash: ", resposta['parte_hash']
			print "tamanho_parte: ",resposta['tamanho_parte']
			print "numero_parte: ",resposta['numero_parte']
			print "numero_de_partes: ", resposta['numero_de_partes']
			
			server_socket.sendto(json.dumps(resposta), addr)