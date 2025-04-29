class Tuple_space:
    def __init__(self, *args):
        self.tuples = {}
        self.client_connected_count = 0
        self.totaloperations_count = 0
        self.read_count = 0
        self.get_count = 0
        self.put_count = 0

    def read(self, key):
        if key in self.tuples:
           self.read_count += 1
           self.totaloperations_count += 1
           return self.tuples[key]
        else:
            print("Key doesn't exist")
            self.error_count += 1
            return ''

        def get(self,key):
        if key in self.tuples:
            del self.tuples[key]
            self.totaloperations_count += 1
            self.get_count += 10
            return self.tuples[key]
        else:
            print("Key doesn't exist, getting fails")
            return ''

    def put(self,key,value):
        if key not in self.tuples:
            self.tuples[key] = value
            self.put_count += 1
            self.totaloperations_count += 1
            return 0
        else:
            print("Key already exists, putting fails")
            self.error_count += 1
            return 1

    def calculations_dataNeeded(self):
        tuples_tupleNumber = len(self.tuples)
        average_key_size = sum(len(k) for k in self.tuples.keys())/tuples_tupleNumber
        average_value_size = sum(len(v) for v in self.tuples.values())/tuples_tupleNumber
        average_tuple_size = average_key_size + average_value_size

        return {
            "tuples number": tuples_tupleNumber,
            "average key size": average_key_size,
            "average value size": average_value_size,
            "average tuple size": average_tuple_size,
            "total operations count": self.totaloperations_count,
            "read count": self.read_count,
            "get count": self.get_count,
            "put count": self.put_count,
            "error count": self.error_count,
            "client count": self.client_connected_count
        }

# handle clients' requests
def handle_clients(client_socket, client_address,tuple_space):
    tuple_space.client_connected_count += 1
    print(f"New client connected from {client_address}")
    try:
        # use a while loop to receieve clients' requests
        while true:
            message_size = client_socket.recv(3).decode("utf-8")
            message_inf = client_socket.recv(int(message_size)-3).decode("utf-8")
            message = message_size +' '+ message_inf
            operation_inf = message_inf[0]
            key_value = message_inf[2:].split(' ', 1)
            key = key_value[0]
            value = key_value[1]

            response_final = ''
            if operation_inf == "R":
                v = tuple_space.read(key)
                if v:
                    response = f'OK {(key,value)}read'
                    # normalize The response as ‘NNN’
                    response_final = f'{str(len(response)+4).zfill(3)} {response}'
                else:
                    response = f'ERR {key} does not exist'
                    response_final = f'{str(len(response)+4).zfill(3)} {response}'
            elif operation_inf == "G":
                v = tuple_space.get(key)
                if v:
                    response = f'OK {(key,value)}get'
                    response_final = f'{str(len(response)+4).zfill(3)} {response}'
                else:
                    response = f'ERR {key} does not exist'
                    response_final = f'{str(len(response)+4).zfill(3)} {response}'
            elif operation_inf == "P":
                e = tuple_space.get(key,value)
                if e == 0:
                    response = f'OK {(key,value)}put'
                    response_final = f'{str(len(response)+4).zfill(3)} {response}'
                elif e==1:
                    response = f'ERR {key} already exists'
                    response_final = f'{str(len(response)+4).zfill(3)} {response}'

            response_final = client_socket.sendall(response_final.encode("utf-8"))
    except Exception as e:
        print(f'Error handling client {client_address}')
    finally:
        client_socket.close()
















