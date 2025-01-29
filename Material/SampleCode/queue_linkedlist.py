class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self, limit=10):
        self.front_node = None
        self.back_node = None
        self.limit = limit
        self.size = 0

    # def __str__(self):
    #     current = self.front_node
    #     if current != None:
    #         print(current.value)
    #         current = current.next
    #     return super().__str__()
    
    # def is_full(self):
    #     return self.size >= self.limit

    # def is_empty(self):
    #     return self.size <= 0
    
    # def peek(self):
    #     if self.front_node != None:
    #         return self.front_node.value
    #     print("Nothing to seek")
    #     return None
    
    def deque(self):
        if self.front_node != None:
            rmfn = self.front_node
            self.front_node = self.front_node.next
            print("front node: ", self.front_node.value)
            print("back node: ", self.back_node.value)
            print("\n")
            return rmfn.value
        print("Nothing to deque")
        return None
    
    def enque(self, value):
        node = Node(value)
        if self.back_node != None:
            self.back_node.next = node
            self.back_node = node
        self.back_node = node
        if self.front_node == None:
            self.front_node = node
        print("front node: ", self.front_node.value)
        print("back node: ", self.back_node.value)
        print("\n")
        return node.value

q = QueueLinkedList(5)

q.enque(10)
q.enque(9)
q.enque(8)

# print(q)

q.deque()
q.deque()
q.deque()