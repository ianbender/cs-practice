'''
Practice implementing Linked Lists
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)


    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = Node(data)
        current.next = self.head
        self.head = current


    def delete(self, data):
        if self.head is None: return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


    # Display in the REPL the same as a Python list
    def __repr__(self):
        if self.head is None: return "[]"

        data = []
        current = self.head
        while True:
            data.append(current.data)
            current = current.next
            if current is None: break

        return f"[{','.join(map(str, data))}]"
