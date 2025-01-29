class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1
        print("+", self.top.value)
        return self.top.value

    def pop(self):
        if self.size >= 0:
            rmn = self.top
            self.top = self.top.next
            print("-", rmn.value)
            self.size -= 1
            return rmn.value
        print("Stack is empty!")
        return None
    
    def peek(self):
        if self.top == None:
            print("Stack is empty")
            return None
        return self.top.value
    
    def is_empty(self):
        return self.size <= 0
    
    def __str__(self):
        current = self.top
        while current != None:
            print(current.value)
            current = current.next
        return super().__str__()

s = StackLinkedList()

s.push(10)
s.push(9)
s.push(8)
s.push(7)
print(s)

s.pop()
s.pop()
print(s)

print(s.peek())
print(s.is_empty())

s.pop()
s.pop()
print(s)

print(s.peek())
print(s.is_empty())