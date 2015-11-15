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
	server_socket = socket(AF_INET, SOCK_DGRAM) # realiza a conexao com o servidor
	server_socket.bind(address)
	lista_de_arquivos=[] #lista de arquivos
	lista_de_arquivos = funcoes.carregaArquivos(lista_de_arquivos) #chama funcao para carregar arquivos na lista
	while(1):
		#print "Listening - Server - Aguarda por requisicoes
		requisicao, addr = server_socket.recvfrom(30000) # servidor recebe requisicao do cliente
		requisicao = json.loads(requisicao)

		# Verifica a TAG
		if requisicao['tag'] == "RequisitarDownload": # Se a requisicao for por um download, a funcao buscaDados eh chamada para buscar a parte requerida
			resposta = json.dumps(funcoes.buscaDados(requisicao, lista_de_arquivos))
			server_socket.sendto(resposta, addr)


		if requisicao['tag'] == "ObterRequisicaoPeers": # Se a requisicao for por um peer,
			funcoes.addPeers(mutex, listaPeers, requisicao) # vai adicionar peer na lista caso o ip do mesmo ainda nao conste nela
			funcoes.insereListaPeers(mutex,requisicao, listaDeHashPeers)
			data = { 'tag': "ObterRespostaPeers",
				 'peers': listaPeers
			}
			server_socket.sendto(json.dumps(data), addr)


		if requisicao['tag'] == "OferecerArquivo": # Se a requisicao for a oferta de um arquivo,
			#tenta inserir na lista de hash de arquivos o peer que ofereceu o arquivo
			funcoes.insereListaArquivos(mutex,requisicao, listaDeHashArquivos) 
