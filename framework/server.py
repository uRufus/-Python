import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8001)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    print(' Server is ready for work')
    client, address = server_socket.accept()
    print(f'{address} connected')
    data = client.recv(1024).decode('UTF-8')
    print(f'Data received: {data}')
    client.sendall('Hello from server\n'.encode('UTF-8'))
    client.close()
