import unittest
import socket
import threading
import time
import os

# Simple function to simulate HTTP client requests
def send_request(path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 3000))
    client_socket.sendall(f"GET {path} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

class TestHTTPServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the server in a background thread before tests run
        cls.server_thread = threading.Thread(target=cls.start_server)
        cls.server_thread.start()
        time.sleep(1)  # Wait for the server to start

    @classmethod
    def start_server(cls):
        # The server code to be tested
        SERVER_HOST = '0.0.0.0'
        SERVER_PORT = 3000

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)

        while True:
            client_socket, client_address = server_socket.accept()
            request = client_socket.recv(1500).decode()

            if not request:
                client_socket.close()
                continue

            headers = request.split('\n')
            if len(headers) > 0:
                first_header_components = headers[0].split()

                if len(first_header_components) >= 2:
                    http_method = first_header_components[0]
                    path = first_header_components[1]

                    if http_method == 'GET':
                        try:
                            if path == '/':
                                content = "Hello, world!"
                            elif path == '/book':
                                content = '{"book": "example"}'
                            else:
                                raise FileNotFoundError
                            response = f'HTTP/1.1 200 OK\n\n{content}'
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

    @classmethod
    def tearDownClass(cls):
        # Stop the server after tests
        cls.server_thread.join()

    def test_valid_get_root(self):
        response = send_request('/')
        self.assertIn("HTTP/1.1 200 OK", response)
        self.assertIn("Hello, world!", response)

    def test_valid_get_book(self):
        response = send_request('/book')
        self.assertIn("HTTP/1.1 200 OK", response)
        self.assertIn('{"book": "example"}', response)

    def test_404_for_invalid_path(self):
        response = send_request('/invalidpath')
        self.assertIn("HTTP/1.1 404 Not Found", response)
        self.assertIn("Page not found.", response)

    def test_405_for_post_method(self):
        # Send a POST request
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 3000))
        client_socket.sendall(f"POST / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()
        self.assertIn("HTTP/1.1 405 Method Not Allowed", response)

    def test_400_for_malformed_request(self):
        # Send a malformed request
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 3000))
        client_socket.sendall(b"GET HTTP/1.1\r\nHost: localhost\r\n\r\n")  # Missing path
        response = client_socket.recv(1024).decode()
        client_socket.close()
        self.assertIn("HTTP/1.1 400 Bad Request", response)
        self.assertIn("Invalid request format.", response)

if __name__ == "__main__":
    unittest.main()
