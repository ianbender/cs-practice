'''
Practice implementing Heaps
A heap is a binary tree where:
- The root node is the minimum value (min heap)
or
- The root node is the maximum value (max heap)

Inserts are top-to-bottom and left-to-right
A small value added to the bottom of a heap bubbles up to the appropriate position
'''

class Heap:

    def __init__(self):
        self.capacity = 10
        self.size = 0
        # allocate a specific amount of space
        self.list = [None] * self.capacity


    def __get_left_child_index(parent_index): return 2 * parent_index + 1
    def __get_right_child_index(parent_index): return 2 * parent_index + 2
    def __get_parent_index(child_index): return (child_index - 1) / 2

    def __has_left_child(index): return self.__get_left_child_index(index) < size
    def __has_right_child(index): return self.__get_right_child_index(index) < size
    def __has_parent(index): return self.__get_parent_index(index) >= 0

    def __left_child(index): return self.list[self.__get_left_child_index(index)]
    def __right_child(index): return self.list[self.__get_right_child_index(index)]
    def __parent(index): return self.list[self.__get_parent_index(index)]


    def swap(first_index, second_index):
        temp = self.list[first_index]
        self.list[first_index] = self.list[second_index]
        self.list[second_index] = temp


    # Doubles the size of the list
    def check_capacity(self):
        if self.capacity == self.size:
            self.list.extend([None] * self.capacity)
            self.capacity *= 2


    def peek(self):
        if size == 0: raise Exception('Heap is empty')
        return self.list[0] if self.size > 0 else None


    def remove(self):
        if size == 0: raise Exception('Heap is empty')
        item = self.list[0]
        self.list[0] = self.list[size - 1]
        self.size -= 1
        self.heap_down()
        return item


    def add(self, item):
       self.check_capacity()
       self.list[size] = item
       self.size += 1
       self.heap_up()


    def heap_up():
        pass


    def heap_down():
        pass


    def __repr__(self):
        return str(self.list)
