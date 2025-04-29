class Tuple_space:
    def __init__(self, *args):
        self.tuples = {}
        self.client_connected_count = 0
        self.totaloperations_count = 0
        self.read_count = 0
        self.get_count = 0
        self.put_count = 0


    