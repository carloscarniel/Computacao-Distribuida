from threading import Thread, Lock
import parametros 
import servidor
import cliente
import json
import funcoes
import hashlib
<<<<<<< HEAD

hasher = hashlib.sha256()
t1=0
=======
import testandoDHT

listaDeHashPeers = []
listaDeHashArquivos = []
funcoes.inicializaListaPeers(listaDeHashPeers)
funcoes.inicializaListaArquivos(listaDeHashArquivos)
>>>>>>> origin/master

print 'Hash do Peer Local:',parametros.meuHash
print 'Hash do Peer Local em mod4:',funcoes.hashMod4(parametros.meuHash)

#cadastra um servidor na lista
listaPeers = [{'ip': parametros.ipServer,
			'porta': parametros.portServer,
			 'hash': 'abcd'}]

mutex = Lock()
t1 = Thread(target=servidor.Servidor, args=(mutex,listaPeers,listaDeHashArquivos,listaDeHashPeers))
t1.start()

<<<<<<< HEAD
t2=Thread(target=cliente.Cliente, args=(mutex,listaPeers))
t2.start()
t2.join()
=======
for i in range(50):
	t2 = Thread(target=testandoDHT.ClienteOffer, args=(mutex,listaDeHashArquivos,parametros.meuHash)) #no original(clienteNovo) param.: mutex,listaPeers,listaArquivos, config.meuHash
	t2.start()
	t2.join()
>>>>>>> origin/master

for j in range(50):
	t3 = Thread(target=testandoDHT.ClientePeers, args=(mutex,parametros.meuHash)) #no original(clienteNovo) param.: mutex,listaPeers,config.meuHash
	t3.start()
	t3.join()

<<<<<<< HEAD
t3=Thread(target=cliente.Cliente2, args=(mutex,listaPeers))
t3.start()
t3.join()

t4 = Thread(target=cliente.ClientePeers, args=(mutex,listaPeers))
t4.start()
t4.join()

#t5 = Thread(target=cliente.ClientePeers, args=(mutex,listaPeers))
#t5.start()
#t5.join()
=======
t4 = Thread(target=testandoDHT.reqListas, args=(listaDeHashPeers,listaDeHashArquivos)) 
t4.start()
t4.join()
>>>>>>> origin/master
