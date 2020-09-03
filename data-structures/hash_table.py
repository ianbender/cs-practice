from linked_list import LinkedList


class HashTable:

    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.list = [LinkedList()] * self.capacity

    # Doubles the size of the list
    def check_capacity(self):
        if self.capacity == self.size:
            self.list.extend([LinkedList()] * self.capacity)
            self.capacity *= 2

    def get_hash_index(self, key):
        return hash(key) % self.capacity

    def get_hash_value(self, key):
        if self.size == 0:
            raise Exception('Hash table is empty')
        index = self.get_hash_index(key)

        return self.list[index]

    # TODO: Implement collision resolution
    def store_hash_value(self, value):
        self.check_capacity()

        index = self.get_hash_index(value)
        self.list[index].append(value)
        self.size += 1
