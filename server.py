import socket
import time
import threading


class Tuple_space:
    def __init__(self):
        self.tuples = {}
        self.client_connected_count = 0
        self.totaloperations_count = 0
        self.read_count = 0
        self.get_count = 0
        self.put_count = 0
        self.error_count = 0
        self.lock = threading.Lock()

    def read(self, key):
           if key in self.tuples:
            self.read_count += 1
            self.totaloperations_count += 1
            return self.tuples[key]
           else:
            #print(f"{key} doesn't exist, reading fails")
            self.error_count += 1
            return ''


    def get(self,key):
        if key in self.tuples:
            value = self.tuples[key]
            del self.tuples[key]
            self.totaloperations_count += 1
            self.get_count += 1
            return value
        else:
            #print(f"{key} doesn't exist, getting fails")
            self.error_count += 1
            return ''

    def put(self,key,value):
        if key not in self.tuples:
            self.tuples[key] = value
            self.put_count += 1
            self.totaloperations_count += 1
            return 0
        else:
            #print(f"{key} already exists, putting fails")
            self.error_count += 1
            return 1

    def calculations_dataNeeded(self):
        tuples_tupleNumber = len(self.tuples)
        if tuples_tupleNumber == 0:
            print("No tuples to report on yet.")
            return
        average_key_size = sum(len(k) for k in self.tuples.keys())/tuples_tupleNumber
        average_value_size = sum(len(v) for v in self.tuples.values())/tuples_tupleNumber
        average_tuple_size = average_key_size + average_value_size

        print(f"tuples number: {tuples_tupleNumber}")
        print(f"average key size: {average_key_size}")
        print(f"average value size: {average_value_size}")
        print(f"average tuple size: {average_tuple_size}")
        print(f"total operations count: {self.totaloperations_count}")
        print(f"read count: {self.read_count}")
        print(f"get count: {self.get_count}")
        print(f"put count: {self.put_count}")
        print(f"error count: {self.error_count}")
        print(f"client count: {self.client_connected_count}")

# Create a lock to restrict the access to the server.
lock = threading.Lock()

# handle clients' requests
def handle_clients(client_socket, client_address,tuple_space):
    tuple_space.client_connected_count += 1
    print(f"New client connected from {client_address}")
    try:
        # receieve clients' requests
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            parts = message.split()
            operation_inf = parts[1]
            key = parts[2]
            value = parts[3] if len(parts) > 3 else ''
            response = ''
            # use lock to avoid multiple threads accessing.
            lock.acquire()
            if operation_inf == "R":
                v = tuple_space.read(key)
                if v:
                    response = f'OK {(key,v)} read'
                else:
                    response = f'ERR {key} does not exist'
            elif operation_inf == "G":
                v = tuple_space.get(key)
                if v:
                    response = f'OK {(key,v)} removed'
                else:
                    response = f'ERR {key} does not exist'
            elif operation_inf == "P":
                e = tuple_space.put(key,value)
                if e == 0:
                    response = f'OK {(key,value)} added'
                elif e == 1:
                    response = f'ERR {key} already exists'
            # else:
            #      response = f"ERR invalid command"
            response_final = f"{str(len(response)+4).zfill(3)} {response}"
            lock.release()
            # send responses to clients
            client_socket.sendall(response_final.encode("utf-8"))
    except Exception as e:
        print(f'Error handling client {e}')
    finally:
        client_socket.close()


def start_sever():
    host = 'localhost'
    port = 51234
    tuple_space = Tuple_space()
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_socket.bind((host, port))
    sever_socket.listen(5)

    print("Sever is running and ready to accept multiple clients")
    def printinfor_thread(tuple_space):
        while True:
            time.sleep(10)
            tuple_space.calculations_dataNeeded()

    threading.Thread(target=printinfor_thread, args=(tuple_space,), daemon=True).start()


    try:
        while True:
            client_socket, client_address = sever_socket.accept()
            client_thread = threading.Thread(target=handle_clients, args=(client_socket, client_address, tuple_space))
            client_thread.start()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, shutting down")
    finally:
        sever_socket.close()


if __name__ == '__main__':
    start_sever()
















