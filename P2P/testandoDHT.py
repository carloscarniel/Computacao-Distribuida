import parametros
import funcoes
import hashlib
import random
import json
import time
import binascii
from socket import *

def ClienteOffer(mutex,listaArquivos, meuHash): # Criacao de peers com porta e hashes (do peer e do arquivo) aleatorios
	h = hashlib.sha256() # Obtem um hash local para ser usado como hash do peer
	arq = hashlib.sha256() # Obtem um hash local para ser usado como hash de um arquivo qualquer a ser oferecido
	h.update(str(random.randint(1,50))) # Atualiza hash do peer com um valor random entre 22 e 30 (assim, hashs diferentes simularao peers diferentes)
	arq.update(str(random.randint(20,200))) # Atualiza hash do arquivo com um valor random entre 22 e 30 
	meuHash = h.hexdigest()
	address = (parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	data = { "tag": "OferecerArquivo",
			 "DonoArquivoOf": {"ip": parametros.ipClient, "port": parametros.portClient + random.randint(1,50), "hash": meuHash},
			 "HashDoOf": arq.hexdigest() # hash de algum arquivo
		   }
	client_socket.sendto(json.dumps(data), address)

def ClientePeers(mutex,meuHash): # Criacao de peers aleatorios (hash random para criar varios diferentes)
	h = hashlib.sha256() # Obtem um hash local para ser usado como hash do peer
	h.update(str(random.randint(1,50))) # Atualiza hash do peer com um valor random entre 22 e 30 (assim, hashs diferentes simularao clientes diferentes)
	address = (parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	data = { "tag": "ObterRequisicaoPeers",
			 "sender": {"ip": parametros.ipClient, "port": parametros.portClient + random.randint(1,50), "hash": h.hexdigest() }
		   }
	client_socket.sendto(json.dumps(data), address)
	resposta, addr = client_socket.recvfrom(30000)

def reqListas(listaDeHashPeers,listaDeHashArquivos):
	while(1):
		time.sleep(5)
		print 'LISTA PEERS'
		for l in listaDeHashPeers:
			if(l['peer'] != None):
				print l['hash'],  l['peer'], funcoes.hashMod4(l['peer']['hash'])
				print
		print
		print 'LISTA ARQUIVOS'
		for l in listaDeHashArquivos:
			if(l['peer'] != None):
				print l['hash'],  l['peer'], funcoes.hashMod4(l['peer']['hash'])
				print
				
