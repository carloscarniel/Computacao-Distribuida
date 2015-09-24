from socket import*
import parametros 
import sys
import binascii
import json
import funcoes
import time
import math
import select
import hashlib

def Cliente(mutex,listaPeers):
	arquivo='teste.rar'
	arquivoFinal='testando.rar'
	hashArquivoTeste1=funcoes.hashDoArquivo(arquivo)
	address=(parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	i=0
	f=open(arquivoFinal, "wb")
	while(True):
		data = { "tag": "DownloadRequest",
				 "hash": hashArquivoTeste1,
				 "numero_parte": i
				}
		print i		
		client_socket.sendto( json.dumps(data), address)
		resposta, addr = client_socket.recvfrom(3000)
		resposta = json.loads(resposta)
		f.write(binascii.a2b_base64(resposta['parte']))
		print data
		if len(resposta['parte']) < 1024:
			break
		i+=1		
	f.close()
	if funcoes.hashDoArquivo(arquivo) == funcoes.hashDoArquivo(arquivoFinal):
		print 'Arquivo transferido e verificdo com sucesso'
	print("Finalizado Cliente")



def Cliente2(mutex,listaPeers):
	arquivo2='teste2.rar'
	arquivoFinal2='testando2.rar'
	hashArquivoTeste2=funcoes.hashDoArquivo(arquivo2)
	address=(parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	i=0
	f=open(arquivoFinal2, "wb")
	while(True):
		data = { "tag": "DownloadRequest",
				 "hash": hashArquivoTeste2,
				 "numero_parte": i
				}
		print i		
		client_socket.sendto( json.dumps(data), address)
		resposta, addr = client_socket.recvfrom(3000)
		resposta = json.loads(resposta)
		f.write(binascii.a2b_base64(resposta['parte']))
		print data
		if len(resposta['parte']) < 1024:
			break
		i+=1		
	f.close()
	if funcoes.hashDoArquivo(arquivo2) == funcoes.hashDoArquivo(arquivoFinal2):
		print 'Arquivo transferido e verificdo com sucesso'
	print("Finalizado Cliente")

def ClientePeers(mutex,listaPeers):

	while(1):
		hasher = hashlib.sha256()
		j={"ip": parametros.ipClient, "porta": parametros.portClient, "hash": hasher.hexdigest()}
		for i in listaPeers:
			if i!=j:
				address=(i['ip'], i['porta'])
				client_socket = socket(AF_INET, SOCK_DGRAM)
				data = {"tag": "GetPeersRequest",
						"sender":{"ip":parametros.ipClient, 
						"porta":parametros.portClient, "hash": hasher.hexdigest()}
						}
				client_socket.sendto(json.dumps(data), address)				
				resposta, addr=client_socket.recvfrom(2500)	
				lista = json.loads(resposta)
				print lista['peers']
				resposta = json.loads(resposta)
				funcoes.appendLista(listaPeers,resposta['peers'], mutex)
				print "foi2"
		time.sleep(5)