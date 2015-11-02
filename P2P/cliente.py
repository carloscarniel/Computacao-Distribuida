from socket import*
import parametros 
import sys
import binascii
import json
import funcoes
<<<<<<< HEAD
import time
import math
import select
import hashlib
=======
import random
import time
import hashlib
import math
import select

#Cliente tbm recebe mutex e lista de peers como parametro. Pode haver clientes que fazem requisicao de download e de peers

listaCliente = []
>>>>>>> origin/master

def Cliente(mutex,listaPeers):
	arquivo = 'teste1.rar'
	arquivoFinal = 'minhacopia.rar'
	hashArquivoTeste1 = funcoes.hashDoArquivo(arquivo)
	address = (parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	i = 0
	f = open(arquivoFinal, "wb")
	while(True):
		data = { "tag": "RequisitarDownload",
				 "hash": hashArquivoTeste1,
				 "numero_parte": i
<<<<<<< HEAD
				}
		print i		
		client_socket.sendto( json.dumps(data), address)
=======
			   }
		client_socket.sendto(json.dumps(data), address)

>>>>>>> origin/master
		resposta, addr = client_socket.recvfrom(3000)
		resposta = json.loads(resposta)
		f.write(binascii.a2b_base64(resposta['part'])) # vai gravar os dados recebidos convertidos para formato binario no arquivo
		if len(resposta['part']) < 1024:
			break
		i+=1
	f.close()
<<<<<<< HEAD
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
=======
	print "Finalizando Cliente.."


def ClientePeers(mutex,listaPeers,meuHash):
	while(1):
		for i in listaPeers:
			if i['ip'] != parametros.ipClient:
				address = (i['ip'], i['port'])
				client_socket = socket(AF_INET, SOCK_DGRAM)
				data = { "tag": "ObterRequisicaoPeers",
						 "sender": {"ip": parametros.ipClient, "port": parametros.portClient, "hash": parametros.meuHash }
					   }
				client_socket.sendto(json.dumps(data), address)
				resposta, addr = client_socket.recvfrom(2500)
				resposta = json.loads(resposta)
				funcoes.appendLista(listaPeers,resposta['peers'], mutex)
		time.sleep(5)
		
def ClienteOffer(mutex,listaPeers,listaArquivos, meuHash):
	arq = hashlib.sha256()
	while(1):
		arq.update(str(random.randint(20,200)))
		hashArquivo = arq.hexdigest()
		for i in listaPeers:
			if i['ip'] != parametros.ipClient:
				address = (i['ip'], i['port'])
				client_socket = socket(AF_INET, SOCK_DGRAM)
				data = { "tag": "OferecerArquivo",
						 "DonoArquivoOf": {"ip": parametros.ipClient, "port": parametros.portClient, "hash": parametros.meuHash},
						 "HashDoOf": hashArquivo # hash do arquivo oferecido
					   }
				client_socket.sendto(json.dumps(data), address)
		time.sleep(10)
>>>>>>> origin/master
