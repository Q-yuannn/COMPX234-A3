import socket
import threading


def client_task(file_path):

    host = 'localhost'
    port = 51234
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    with open(file_path, 'r') as f:
        lines = f.readlines()
    try:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Reduce the information in the file
            parts = line.split(' ', 2)
            operation = parts[0].upper()
            key = parts[1] if len(parts) > 1 else ''
            value = parts[2] if len(parts) > 2 else ''


            if operation not in ('PUT', 'GET', 'READ'):
                print(f"Invalid operation: {operation}")
                continue

            # if operation in ('GET', 'READ'):
            #     if len(parts) < 2:
            #         print(f"Missing key in line: {line}")
            #         continue
            #     key = parts[1]
            #     if len(key) > 970:
            #         print(f"Invalid size: key too long.")
            #         continue
            #     message_inf = f"{operation[0]} {key}"
            if len(key) + len(value) > 970:
                print("Invalid size: key + value exceeds 970 characters.")
                continue
            if operation == 'READ':
                message_inf = f'R {key}'
            elif operation == 'GET':
                message_inf = f'G {key}'
            elif operation == 'PUT':
                if len(parts) < 3:
                    print(f"Missing value in line: {line}")
                    continue
                message_inf = f"P {key} {value}"
            # format the request
            message_normalization = f"{str(len(message_inf) + 4).zfill(3)} {message_inf}"

            client_socket.sendall(message_normalization.encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8')
            print(f"{operation} {key} {value}: {response[4:]}")

    except Exception as e:
        print('error:',str(e))
    finally:
        client_socket.close()

def main():
    clients = []
    for i in range(10):
       t = threading.Thread(target=client_task, args=(rf"D:\Github_files\lab3\test\client_{i+1}.txt",))
       clients.append(t)
       t.start()

    for t in clients:
        t.join()

if __name__ == '__main__':
    main()




