from socket import *
import parametros 
import sys
import binascii
import json
import funcoes
import select
import hashlib

<<<<<<< HEAD
def Servidor(mutex,listaPeers):
	address=(parametros.ipServer, parametros.portServer)
=======

def Servidor(mutex,listaPeers,listaDeHashArquivos,listaDeHashPeers):
	address = (parametros.ipClient, parametros.portClient) # address recebe ip e porta do cliente (local meu)
>>>>>>> origin/master
	server_socket = socket(AF_INET, SOCK_DGRAM)
	server_socket.bind(address)
	lista_de_arquivos=[] #lista de arquivos
	lista_de_arquivos = funcoes.carregaArquivos(lista_de_arquivos) #chama funcao para carregar arquivos na 
	while(1):
<<<<<<< HEAD
		print "escutando"
		requisicao, addr = server_socket.recvfrom(1024)
		requisicao = json.loads(requisicao)
		print "passo"
		if requisicao['tag'] == "DownloadRequest":
			resposta = json.dumps(funcoes.buscaDados(requisicao, lista_de_arquivos))
			server_socket.sendto(resposta, addr)
		if requisicao['tag'] == "GetPeersRequest":
			print "req"
			funcoes.addPeers(mutex, listaPeers, requisicao) # vai adicionar peer na lista caso o ip do mesmo ainda nao conste nela - retirar teste
			data = { 'tag': "GetPeersResponse",
				 'peers': listaPeers
			}
			server_socket.sendto(json.dumps(data), addr)
			
=======
		#print "Listening - Server"
		requisicao, addr = server_socket.recvfrom(1024) # servidor recebe requisicao do cliente
		requisicao = json.loads(requisicao)
		# Verifica a TAG
		if requisicao['tag'] == "RequisitarDownload":
			resposta = json.dumps(funcoes.buscaDados(requisicao, lista_de_arquivos))
			server_socket.sendto(resposta, addr)
		if requisicao['tag'] == "ObterRequisicaoPeers":
			funcoes.addPeers(mutex, listaPeers, requisicao) # vai adicionar peer na lista caso o ip do mesmo ainda nao conste nela - retirar teste
			funcoes.insereListaPeers(mutex,requisicao, listaDeHashPeers)
			data = { 'tag': "ObterRespostaPeers",
				 'peers': listaPeers
			}
			server_socket.sendto(json.dumps(data), addr)
		if requisicao['tag'] == "OferecerArquivo":
			#print 'Hash inserir:', func.hashMod(requisicao['HashDoOf'])
			funcoes.insereListaArquivos(mutex,requisicao, listaDeHashArquivos) #tenta inserir na lista de arquivos o peer que ofereceu o arquivo
>>>>>>> origin/master
