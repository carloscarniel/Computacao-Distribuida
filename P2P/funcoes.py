import math
import os
import glob


def carregaArquivos(lista_de_arquivos):
	indices = 0
#	for file in glob.glob('*.rar'):

	arq=open("teste.rar","rb")
	arq.seek(0,0)
	partes=0
	totalPartes = math.ceil(os.path.getsize("teste.rar")/8192)

	while True :
		linha=arq.read(8192)
		if linha == '':
			break
		lista_de_arquivos.append({"nome":"teste.rar", 	
				"totalPartes": totalPartes,
				"parte": partes,
				"data": linha })
		partes += 1
		indices +=1
	arq.close()
	return lista_de_arquivos