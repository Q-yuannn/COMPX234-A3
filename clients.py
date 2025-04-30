import socket
def client_task(file_path):
    host = 'localhost'
    port = 51234
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
