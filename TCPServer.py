from socket import *
import os

porta = 12000

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(('', porta))
servidor.listen(1)

print("READY")

while True:
    socket_conexao, endereco = servidor.accept()
    requisicao = socket_conexao.recv(1024).decode()
    
    if requisicao.startswith('GET'):
        nome_arquivo = requisicao.split()[1]
        if nome_arquivo == '/':
            nome_arquivo = '/index.html'
            
        if os.path.isfile('.' + nome_arquivo):
            arquivo = open('.' + nome_arquivo, 'rb')
            resposta = arquivo.read()
            arquivo.close()
            cabecalho = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
        else:
            resposta = 'Arquivo não encontrado'.encode()
            cabecalho = 'HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'
    else:
        resposta = 'Método não suportado'.encode()
        cabecalho = 'HTTP/1.1 405 Method Not Allowed\nContent-Type: text/plain\n\n'

    socket_conexao.send(cabecalho.encode() + resposta)
    socket_conexao.close()
