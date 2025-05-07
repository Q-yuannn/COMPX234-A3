import socket
def client_task(file_path):
    host = 'localhost'
    port = 51234
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    with open(file_path, 'r') as f:
        lines = f.readlines()
    try:
        for line in lines:
            line.strip()
            message = line.split(' ',1)
            if len(message) < 2:
                print(f"Invalid line: {line}")
                continue
            operation_inf = message[0]
            if operation_inf == 'READ':
                key = message[1]
                message_length = 4+2+len(key)
                if message_length >= 7 and message_length < 999:
                  message_normalization = str(message_length).zfill(3)+' '+'R'+' '+key
                else:
                    print('Invalid size')
            elif operation_inf == 'GET':
                key = message[1]
                message_length = 4+2+len(key)
                if message_length >= 7 and message_length < 999:
                    message_normalization = str(message_length).zfill(3)+' '+'G'+' '+key
            elif operation_inf == 'PUT':
                message = line.split(' ',2)
                key = message[1]
                value = message[2]
                message_length = 4+3+len(key)+len(value)
                if message_length >= 7 and message_length < 999:
                    message_normalization = str(message_length).zfill(3)+' '+'P'+' '+key+' '+value
        client_socket.sendall(message_normalization.encode('utf-8'))
        response_final = client_socket.recv(1024).decode('utf-8')
        print('Response received:', response_final)
    except Exception as e:
        print('error:'+e)
    finally:
        client_socket.close()

def main():
    clients = []
    for i in repr(10):
       t = threading.Thread(target=client_task, args=(rf"D:\系统与网络\test\client_{i+1}"))
       clients.append(t)
       t.start()

    for t in clients:
        t.join()

if __name__ == '__main__':
    main()




