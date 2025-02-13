class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    def enque(self, value):
        node = Node(value)
        if self.size == 0:
            self.front = node
            self.back = node
            self.size += 1
        else:
            self.back.next = node
            self.back = node
            self.size += 1
    
    def deque(self):
        if self.size == 0:
            print("Queue is empty!")
            return None
        if self.size == 1:
            node = self.front
            self.front = None
            self.back = None
            self.size -= 1
            return node.value
        else:
            node = self.front
            self.front = node.next
            self.size -= 1
            return node.value
    
    def is_empty(self):
        return self.size == 0

    def __str__(self):
        current = self.front
        while current != None:
            print(current.value)
            current = current.next
        return super().__str__()

q = QueueLinkedList()
q.enque(10)
q.enque(9)
q.enque(8)
print(q)

q.deque()
q.deque()
q.deque()
print(q.is_empty())
q.deque()
print(q)