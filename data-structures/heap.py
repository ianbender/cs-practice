"""
Practice implementing Heaps
A heap is a binary tree where:
- The root node is the minimum value (min heap)
or
- The root node is the maximum value (max heap)

Inserts are top-to-bottom and left-to-right
A small value added to the bottom of a heap bubbles up to the appropriate position
"""


class Heap:

    def __init__(self):
        self.capacity = 10
        self.size = 0
        # allocate a specific amount of space
        self.list = [None] * self.capacity

    @staticmethod
    def get_left_child_index(parent_index):
        return 2 * parent_index + 1

    @staticmethod
    def get_right_child_index(parent_index):
        return 2 * parent_index + 2

    @staticmethod
    def get_parent_index(child_index):
        return int((child_index - 1) / 2)

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.list[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.list[self.get_right_child_index(index)]

    def parent(self, index):
        return self.list[self.get_parent_index(index)]

    def swap(self, first_index, second_index):
        temp = self.list[first_index]
        self.list[first_index] = self.list[second_index]
        self.list[second_index] = temp

    # Doubles the size of the list
    def check_capacity(self):
        if self.capacity == self.size:
            self.list.extend([None] * self.capacity)
            self.capacity *= 2

    def peek(self):
        if self.size == 0: raise Exception('Heap is empty')
        return self.list[0] if self.size > 0 else None

    def pluck(self):
        if self.size == 0: raise Exception('Heap is empty')
        item = self.list[0]
        self.list[0] = self.list[self.size - 1]
        self.list[self.size - 1] = None
        self.size -= 1
        self.heap_down()
        return item

    def add(self, item):
        self.check_capacity()
        self.list[self.size] = item
        self.size += 1
        self.heap_up()

    def heap_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.list[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heap_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_index = self.get_left_child_index(index)
            if self.has_right_child(index) and (self.right_child(index) < self.left_child(index)):
                smaller_index = self.get_right_child_index(index)

            if self.list[index] < self.list[smaller_index]:
                break

            self.swap(index, smaller_index)
            index = smaller_index

    def __repr__(self):
        return str(self.list)


if __name__ == '__main__':
    h = Heap()
    h.add(5)
    h.add(8)
    h.add(3)
    h.peek()
    for i in range(h.size):
        print(h.pluck())
