from socket import *

nome_host = '127.0.0.1'
porta = 12000

client = socket(AF_INET, SOCK_STREAM)
client.connect((nome_host, porta))

req = 'GET / HTTP/1.1\nHost: ' + nome_host + '\n\n'
client.send(req.encode())

res = client.recv(4096).decode()

header, body = res.split('\n\n', 1)
if header.split()[1] == '200':
    print(body)
else:
    print('Erro de resposta do servidor')

client.close()
