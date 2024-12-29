import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f'Listening on port {SERVER_PORT} ...') 

while True: 
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print(f'Connection established with {client_address}') 
    request = client_socket.recv(1500).decode()
    
    if not request:
        print('Received empty request, skipping...')
        client_socket.close()
        continue

    print(request)

    headers = request.split('\n')
    if len(headers) > 0:
        first_header_components = headers[0].split()

        if len(first_header_components) >= 2:
            http_method = first_header_components[0]
            path = first_header_components[1]

            if http_method == 'GET':
                try:
                    if path == '/':
                        fin = open('index.html', 'r')
                    elif path == '/book':
                        fin = open('book.json', 'r')
                    else:
                        raise FileNotFoundError

                    content = fin.read()
                    fin.close()
                    response = 'HTTP/1.1 200 OK\n\n' + content
                except FileNotFoundError:
                    response = 'HTTP/1.1 404 Not Found\n\nPage not found.'
            else:
                response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'
        else:
            response = 'HTTP/1.1 400 Bad Request\n\nInvalid request format.'
    else:
        response = 'HTTP/1.1 400 Bad Request\n\nEmpty request.'

    client_socket.sendall(response.encode())
    client_socket.close()

server_socket.close()
