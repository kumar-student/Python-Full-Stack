class Node:
    def __init__(self, value, pre=None, next=None, index=None):
        self.value = value
        self.pre = pre
        self.next = next
        self.index = index

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def add(self, value):
        if self.size == 0:
            node = Node(value, index=0)
            self.start = node
            self.end = node
            self.size += 1
        else:
            node = Node(value, index=self.end.index+1)
            node.next = self.end
            self.end.pre = node
            self.end = node
            self.size += 1

    def __str__(self):
        current = self.start
        while current != None:
            print(current.index, "->", current.value)
            current = current.pre
        return super().__str__()

l = LinkedList()
l.add(10)
l.add(9)
l.add(8)
print(l)