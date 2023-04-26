import socket

HOST = ''  # endereço IP do servidor
PORT = 8000  # porta em que o servidor irá escutar

# cria o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# faz o bind do socket com o endereço e porta especificados
servidor.bind((HOST, PORT))

# coloca o servidor para escutar por conexões
servidor.listen()

print(f'Servidor TCP escutando em {HOST}:{PORT}...')

while True:
    # aceita uma conexão do cliente
    conexao, endereco_cliente = servidor.accept()
    print(f'Conexão recebida de {endereco_cliente}')

    # lê o conteúdo do arquivo "index.html"
    with open('index.html', 'rb') as arquivo:
        conteudo = arquivo.read()

    # envia o conteúdo do arquivo para o cliente
    conexao.sendall(b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n' + conteudo)

    # fecha a conexão
    conexao.close()
