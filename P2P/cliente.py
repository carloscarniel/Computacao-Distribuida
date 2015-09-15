from socket import*
import parametros 
import sys
import binascii
import json
import funcoes


def Cliente(mutex,listaPeers):
	arquivo='teste.rar'
	arquivoFinal='testando.rar'
	hashArquivoTeste1=funcoes.hashDoArquivo(arquivo)
	address=(parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	i=0
	f=open(arquivoFinal, "wb")
	while(True):
		data = { "tag": "DownloadRequest",
				 "hash": hashArquivoTeste1,
				 "numero_parte": i
				}
		print i		
		client_socket.sendto( json.dumps(data), address)
		resposta, addr = client_socket.recvfrom(30000)
		resposta = json.loads(resposta)
		f.write(binascii.a2b_base64(resposta['parte']))
		print data
		if len(resposta['parte']) < 1024:
			break
		i+=1		
	f.close()
	if funcoes.hashDoArquivo(arquivo1) == funcoes.hashDoArquivo(arquivoFinal):
		print 'Arquivo transferido e verificdo com sucesso'
	printf("Finalizado Cliente")



def Cliente2(mutex,listaPeers):
	arquivo='teste.rar'
	arquivoFinal='testando2.rar'
	hashArquivoTeste1=funcoes.hashDoArquivo(arquivo)
	address=(parametros.ipServer, parametros.portServer)
	client_socket = socket(AF_INET, SOCK_DGRAM)
	i=0
	f=open(arquivoFinal, "wb")
	while(True):
		data = { "tag": "DownloadRequest",
				 "hash": hashArquivoTeste1,
				 "numero_parte": i
				}
		print i		
		client_socket.sendto( json.dumps(data), address)
		resposta, addr = client_socket.recvfrom(30000)
		resposta = json.loads(resposta)
		f.write(binascii.a2b_base64(resposta['parte']))
		print data
		if len(resposta['parte']) < 1024:
			break
		i+=1		
	f.close()
	if funcoes.hashDoArquivo(arquivo1) == funcoes.hashDoArquivo(arquivoFinal):
		print 'Arquivo transferido e verificdo com sucesso'
	printf("Finalizado Cliente")
