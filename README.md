# MANUAL DO USUARIO DO SITE TRADUÇÕES XYZ

# Matricula 201900076829

# TODOS OS COMANDOS DEVEM SER SEGUIDOS A RISCA !!

#  ACESSO AO CLONE DO GIT
```
git clone https://github.com/rayan012a/labredesfinal
```

```
cd labredesfinal
```

# Fazendo o container
```
docker build -t etapa4 .
```
### DEIXAR O SERVIDOR RODANDO
```
docker run -d etapa4
```

### Listar todos os containers (para conseguir o id do etapa4)
```
docker ps
```

### Testa o client.py para ver a pagina funcionando
```
docker exec aadedcab0121 python TCPClient.py
```

### Verificar os arquivos do container !!!
```
docker exec -i -t ba4e23bf3fdd /bin/bash
```
