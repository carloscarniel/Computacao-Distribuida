from parametros import *
import math
import os
import glob
import hashlib
import binascii
import json

def hashDoArquivo(arquivo):
	BLOCKSIZE = 1024
	hasher = hashlib.sha256()
	with open(arquivo, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
#	print hasher.hexdigest()		
	return hasher.hexdigest()


def buscaDados(requisicao, lista_de_arquivos):

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
			
			return resposta
				


def carregaArquivos(lista_de_arquivos):
	indices = 0

	for file in glob.glob('*.rar'):

		arq=open(file,"rb")
		arq.seek(0,0)
		partes=0
		totalPartes = math.ceil(os.path.getsize(file)/1024)

		while True :
			linha=arq.read(1024)
			if linha == '':
				break
			hash_object = hashlib.sha256(linha)
			hex_dig = hash_object.hexdigest()
			lista_de_arquivos.append({"hash_do_arquivo":hashDoArquivo(file), 	
				"totalPartes": totalPartes,
				"parte": partes,
				"hash_da_parte": hex_dig,
				"data": linha })
			partes += 1
			indices +=1
	arq.close()
	return lista_de_arquivos

def appendLista(lista1,lista2, mutex):
	cont=0
	for i in lista2:
		for j in lista1:
			if (i == j):
				cont += 1
		if (cont == 0):
			mutex.acquire()
			lista1.append(i)
			mutex.release()
		else:cont=0	
	print "foi"	

def addPeers(mutex, listaPeers, requisicao):
	print "oloco"
	for i in listaPeers:
		if (i == requisicao['sender']):# and (i['port'] == address[1])):
			return
	novo = {'ip': requisicao['sender']['ip'],
			'porta': requisicao['sender']['porta'],
			}

	data_string = json.dumps(novo)
	mutex.acquire()
	listaPeers.append(json.loads(data_string))
	mutex.release()

