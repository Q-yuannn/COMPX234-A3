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

    