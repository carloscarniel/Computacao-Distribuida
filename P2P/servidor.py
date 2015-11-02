from socket import *
import parametros 
import sys
import binascii
import json
import funcoes
import select
import hashlib


def Servidor(mutex,listaPeers,listaDeHashArquivos,listaDeHashPeers):
	address = (parametros.ipClient, parametros.portClient) # address recebe ip e porta do cliente (local meu)
	server_socket = socket(AF_INET, SOCK_DGRAM)
	server_socket.bind(address)
	lista_de_arquivos=[] #lista de arquivos
	lista_de_arquivos = funcoes.carregaArquivos(lista_de_arquivos) #chama funcao para carregar arquivos na 
	while(1):
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
