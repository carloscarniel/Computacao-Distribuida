from parametros import *
import math
import os
import glob
import hashlib

def hashDoArquivo(arquivo):
	BLOCKSIZE = 8192
	hasher = hashlib.sha256()
	with open(arquivo, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
#	print hasher.hexdigest()		
	return hasher.hexdigest()



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
			lista_de_arquivos.append({"hash_do_arquivo":hashDoArquivo(file), 	
				"totalPartes": totalPartes,
				"parte": partes,
				"hash_da_parte": hex_dig,
				"data": linha })
			partes += 1
			indices +=1
	arq.close()
	return lista_de_arquivos