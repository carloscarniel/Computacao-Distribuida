from threading import Thread, Lock
import parametros 
import servidor
import cliente
from socket import*
import sys
import binascii
import json
import funcoes

t1=0

listaPeers = [{'ip': parametros.ipServer,
			'porta': parametros.portServer }]

mutex=Lock()
t1=Thread(target=servidor.Servidor, args=(mutex,listaPeers))
t1.start()

t2=Thread(target=cliente.Cliente, args=(mutex,listaPeers))
t2.start()
t2.join()


#t3=Thread(target=cliente.Cliente, args=(mutex,listaPeers))
#t3.start()
#t3.join()

t4 = Thread(target=cliente.ClientePeers, args=(mutex,listaPeers))
t4.start()
t4.join()
#t5 = Thread(target=cliente.ClientePeers, args=(mutex,listaPeers))
#t5.start()
#t5.join()
