class StackArray:
    def __init__(self, limit=10):
        self.arr = []
        self.limit = limit
    
    def push(self, value):
        if len(self.arr) <= self.limit :
            self.arr.append(value)
            print("+", value)
            return value
        print("Stack is full!")
        return None
    
    def pop(self):
        if len(self.arr) > 0:
            rme = self.arr[-1]
            del self.arr[-1]
            print("-", rme)
            return rme
        return None

    def peek(self):
        if len(self.arr) > 0:
            return self.arr[-1]
        return None
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def is_full(self):
        return len(self.arr) >= self.limit
    
    def get_size(self):
        return len(self.arr)
    
    def __str__(self):
        if self.get_size() > 0:
            for i in self.arr:
                print(i)
        return super().__str__()

s = StackArray(5)

s.push(10)
s.push(7)
s.push(3)
s.push(-2)
s.push(8)
s.push(6)

print(s)

s.pop()
s.pop()

print(s)

print(s.peek())
