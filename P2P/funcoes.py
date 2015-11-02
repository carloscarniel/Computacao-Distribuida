import parametros
import math
import os
import glob
import hashlib
import json
import binascii

def hashMod4(hashStr): 
	aux = binascii.unhexlify(hashStr) # transforma o hash que esta em hexa em binario e depois em decimal
	final = ''
	for i in aux:
		val = ord(i) % 4
		final = final + str(val)
	return final


def hashDoArquivo(arquivo):
	BLOCKSIZE = 1024
	hasher = hashlib.sha256()
	with open(arquivo, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()


def buscaDados(requisicao, lista_de_arquivos):
	for i in lista_de_arquivos:
			if i['hashArq'] == requisicao['hash'] and i['parte'] == requisicao['numero_parte'] : # achou arquivo e parte
				resposta = { "tag": "DownloadResponse",
				 "part_hash": i['hashParte'],
				 "part_length": len(i['data']),
				 "numero_parte": i['parte'],
				 "number_of_parts": i['totPartes'],
				 "part": binascii.b2a_base64(i['data'])
				}
				return resposta


def carregaArquivos(lista_de_arquivos):
	indices = 0

	for file in glob.glob('*.rar'):

		arq=open(file,"rb")
		arq.seek(0,0)
		partes=0
		totalPartes = math.ceil(os.path.getsize(file)/8192)

		while True :
			linha=arq.read(8192)
			if linha == '':
				break
			hash_object = hashlib.sha256(linha)
			hex_dig = hash_object.hexdigest()
			lista_de_arquivos.append({"hashArq": hashDoArquivo(file),
				   "totPartes": totalPartes,
                   "parte": partes,
                   "hashParte": hex_dig,
				   "data": linha})
			partes += 1
			indices +=1
	arq.close()
	return lista_de_arquivos

def inicializaListaPeers(lista): # recebe a lista vazia de main.py
	auxHash = ''  
	meuHash = hashMod4(parametros.meuHash) # chama a funcao hashMod, passando o hash proprio como parametro
	pos = 0
	for i in range(len(meuHash)+1): #tamanho do hash + 1
		for j in range(4): # 4
			lista.append({"hash": auxHash + str(j), 
						  "peer": None})
		auxHash = auxHash + meuHash[int(pos)]
		if(i < len(meuHash)-1): pos+=1

def inicializaListaArquivos(lista):
	auxHash = ''
	meuHash = hashMod4(parametros.meuHash)
	pos = 0
	for i in range(len(meuHash)+1): #tamanho do hash + 1
		for j in range(4):
			lista.append({"hash": auxHash + str(j),
						  "peer": None}) # Hash + ??
		auxHash = auxHash + meuHash[int(pos)]
		if(i < len(meuHash)-1): pos+=1 # i < (tamanho do hash - 1)
	
#chama no mesmo lugar que adcionava na lista antiga

def addPeers(mutex, listaPeers, requisicao):
	for i in listaPeers:
		if (i == requisicao['sender']):# and (i['port'] == address[1])):
			return
	novo = {'ip': requisicao['sender']['ip'],
			'port': requisicao['sender']['port'],
			'hash': requisicao['sender']['hash']
			}
	data_string = json.dumps(novo)
	mutex.acquire()
	listaPeers.append(json.loads(data_string))
	mutex.release()

def insereListaPeers(mutex, requisicao, listaDeHashPeers):
	#confere quantos numeros iniciais o hash possui em comum com o hash da lista
	hashInsert = hashMod4(requisicao['sender']['hash']) # hash do arquivo oferecido
	#print "print isereListaPeers"
	print hashInsert 
	meuHash = hashMod4(parametros.meuHash)
	cont = 0
	for i in range(len(meuHash)):
		if (meuHash[i] == hashInsert[i]):
			cont+=1
		else: break
		
	if(cont == 0): # se nenhum dos primeiros numeros do hash coincide testa apenas com os 4 prefixs (0,1,2 e 3) 
			for i in listaDeHashPeers:
				if (i['hash'] == hashInsert[0]):
					if (i['peer'] == None): # posicao da lista esta livre, pode inserir
						#insere na lista
						mutex.acquire()
						i['peer'] = requisicao['sender']
						mutex.release()
					else:
						return
			return
	#senao vai continuar e faz a verificacao ate o numero cont de caracteres do hash iguais		
	parcial = ''
	for i in range(cont+1):
		parcial = parcial + hashInsert[i]
		for j in listaDeHashPeers: # percorre toda lista atras da mesma parte do hash
			if(j['hash'] == parcial):
				if(j['peer'] == None):
					#vai inserir na lista
					mutex.acquire()
					j['peer'] = requisicao['sender']
					mutex.release()
					return # retorna com o peer ja inserido
	return # caso nenhum de certo apenas retorna, sem inserir na lista

#Chama a funcao sempre que receber uma oferta de arquivo
def insereListaArquivos(mutex,requisicao, listaDeHashArquivos):
	#confere quantos numeros iniciais o hash possui em comum com o hash da lista
	hashInsert = hashMod4(requisicao['HashDoOf'])
	#print "insereListaArquivos"
	print hashInsert 
	meuHash = hashMod4(parametros.meuHash)
	cont = 0
	for i in range(len(meuHash)):
		if (meuHash[i] == hashInsert[i]):
			cont+=1
		else: break
		
	if(cont == 0): # se nenhum dos primeiros numeros do hash coincide testa apenas com os 4 prefixs (0,1,2 e 3) 
			for i in listaDeHashArquivos:
				if (i['hash'] == hashInsert[0]):
					if (i['peer'] == None): # posicao da lista esta livre, pode inserir
						#insere na lista
						mutex.acquire()
						i['peer'] =  {'ip':requisicao['DonoArquivoOf']['ip'], "port":requisicao['DonoArquivoOf']['port'], 'hash': requisicao['HashDoOf']}
						mutex.release()
					else: return
			return
	#senao vai continuar e faz a verificacao ate o numero cont de caracteres do hash iguais		
	parcial = ''
	for i in range(cont+1):
		parcial = parcial + hashInsert[i]
		for j in listaDeHashArquivos: # percorre toda lista atras da mesma parte do hash
			if(j['hash'] == parcial):
				if(j['peer'] == None):
					#vai inserir na lista
					mutex.acquire()
					j['peer'] = {'ip':requisicao['DonoArquivoOf']['ip'], "port":requisicao['DonoArquivoOf']['port'], 'hash': requisicao['HashDoOf']} # insere na lista
					mutex.release()
					return # retorna com o peer ja inserido
	return # caso nenhum de certo apenas retorna, sem inserir na lista

def appendLista(lista1, lista2, mutex):
	cont=0
	for i in lista2:
		for j in lista1:
			if (i == j):# and (i['port'] == j['port'])): # verifica se ip ja esta na lista para nao repetir peers
				cont+=1
		if cont == 0:
			mutex.acquire()
			lista1.append(i) # se ip nao esta na listapeers adiciona peers
			mutex.release()
		else: cont = 0