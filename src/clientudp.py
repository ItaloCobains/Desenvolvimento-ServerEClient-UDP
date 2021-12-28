import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_INET = para usar o protocolo IP, socket.SOCK_DGRAM = para usar o protocolo UDP

print('[*]CLIENT SOCKET CRIADO COM SUCESSO!!!')

host = 'localhost'
port = 5433
mensagem = 'Olá Servidor'

try:
	print(f'Client: {mensagem}')
	s.sendto(mensagem.encode(), (host, port))#empacotando a mensagem e enviando com pacotes udp para o servidor
	
	dados, servidor = s.recvfrom(4096)
	dados = dados.decode()
	print(dados)
finally:
	print('Client: Fechando a conexâo')
	s.close()


