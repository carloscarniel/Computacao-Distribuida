import parametros
import funcoes
import hashlib
import random
import json
import time
import binascii
from socket import *

def ClienteOffer(mutex,listaArquivos, meuHash):
	h = hashlib.sha256()
	arq = hashlib.sha256()
	h.update(str(random.randint(22,30)))
	arq.update(str(random.randint(20,200)))
	meuHash = h.hexdigest()
	address = (parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	data = { "tag": "OferecerArquivo",
			 "DonoArquivoOf": {"ip": parametros.ipClient, "port": parametros.portClient + random.randint(1,50), "hash": meuHash},
			 "HashDoOf": arq.hexdigest() # hash de algum arquivo
		   }
	client_socket.sendto(json.dumps(data), address)

def ClientePeers(mutex,meuHash):
	h = hashlib.sha256()
	h.update(str(random.randint(22,30)))
	address = (parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	data = { "tag": "ObterRequisicaoPeers",
			 "sender": {"ip": parametros.ipClient, "port": parametros.portClient, "hash": h.hexdigest() }
		   }
	client_socket.sendto(json.dumps(data), address)
	resposta, addr = client_socket.recvfrom(2500)

def reqListas(listaDeHashPeers,listaDeHashArquivos):
	while(1):
		time.sleep(5)
		print 'LISTA PEERS'
		for l in listaDeHashPeers:
			if(l['peer'] != None):
				print l['hash'],  l['peer']
				print
		print
		print 'LISTA ARQUIVOS'
		for l in listaDeHashArquivos:
			if(l['peer'] != None):
				print l['hash'],  l['peer'], funcoes.hashMod4(l['peer']['hash'])
				print
				
