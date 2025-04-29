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




