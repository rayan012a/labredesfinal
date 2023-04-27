FROM python:3-slim
LABEL version="1.0.0" description="tradutor XYZ" maintainer="Rayan Tavares <rayantavaresjjba@academico.ufs.br>"
WORKDIR /usr/src/labredesfinal
COPY . .
EXPOSE 12000
CMD ["python3", "./TCPServer.py"]
