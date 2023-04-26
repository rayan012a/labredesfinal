import socket

HOST = 'localhost'  # endereço IP do servidor
PORT = 8000  # porta em que o servidor está escutando

# cria o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
cliente.connect((HOST, PORT))

# envia uma mensagem para o servidor (opcional)
cliente.sendall(b'Olá, servidor!')

# recebe a resposta do servidor
resposta = cliente.recv(1024)

# exibe a resposta na tela
print(resposta.decode())

# fecha a conexão
cliente.close()
