from threading import Thread, Lock
import parametros 
import servidor
import cliente
import json
import funcoes
import hashlib
import testandoDHT

listaDeHashPeers = []
listaDeHashArquivos = []
funcoes.inicializaListaPeers(listaDeHashPeers) # Inicializa lista de peers como uma tabela DHT
funcoes.inicializaListaArquivos(listaDeHashArquivos) # Inicializa lista de arquivos como uma tabela DHT

print 'Hash do Peer Local:',parametros.meuHash  # Mostra o hash local na tela
print 'Hash do Peer Local em mod4:',funcoes.hashMod4(parametros.meuHash) # Mostra o hash convertido em mod4 para simplificar a utilizacao dos prefixos

#cadastra um servidor na lista
listaPeers = [{'ip': parametros.ipServer,
			'port': parametros.portServer,
			'hash': 'abcd'}]

mutex = Lock()
t1 = Thread(target=servidor.Servidor, args=(mutex,listaPeers,listaDeHashArquivos,listaDeHashPeers))
t1.start()

print
print "Lista de Hashes dos arquivos"
for i in range(50):
	t2 = Thread(target=testandoDHT.ClienteOffer, args=(mutex,listaDeHashArquivos,parametros.meuHash)) #no original(clienteNovo) param.: mutex,listaPeers,listaArquivos, config.meuHash
	t2.start()
	t2.join()

print
print
print "Lista de Hashes dos peers"
for j in range(50):
	t3 = Thread(target=testandoDHT.ClientePeers, args=(mutex,parametros.meuHash)) #no original(clienteNovo) param.: mutex,listaPeers,config.meuHash
	t3.start()
	t3.join()

t4 = Thread(target=testandoDHT.reqListas, args=(listaDeHashPeers,listaDeHashArquivos)) 
t4.start()
t4.join()