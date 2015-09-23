from socket import *
import parametros 
import sys
import binascii
import json
import funcoes
import select


def Servidor(mutex,listaPeers):
	address=(parametros.ipServer, parametros.portServer)
	server_socket = socket(AF_INET, SOCK_DGRAM)
	server_socket.bind(address)
	lista_de_arquivos=[]
	lista_de_arquivos=funcoes.carregaArquivos(lista_de_arquivos)
	while(1):
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