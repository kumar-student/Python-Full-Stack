class QueueArray:
    def __init__(self, limit=10):
        self.arr = []
        self.limit = limit

    def enque(self, value):
        if len(self.arr) >= self.limit:
            print("Queue is full!")
            return None
        self.arr.append(value)
        print("+", self.arr[-1])
        return None

    def deque(self):
        if len(self.arr) == 0:
            print("Queue is empty!")
            return None
        element = self.arr[0]
        del self.arr[0]
        return element

    def get_front(self):
        if len(self.arr) == 0:
            print("Queue is empty!")
            return None
        return self.arr[0]

    def get_end(self):
        if len(self.arr) == 0:
            print("Queue is empty!")
            return None
        return self.arr[-1]

    def get_size(self):
        return len(self.arr)

    def is_full(self):
        return len(self.arr) >= self.limit

    def is_empty(self):
        return len(self.arr) == 0

    def __str__(self):
        if len(self.arr) > 0:
            for i in self.arr:
                print(i)
        return super().__str__()
        

q = QueueArray()

q.enque(5)
q.enque(7)
q.enque(9)
q.enque(10)

print(q)

q.deque()
q.deque()

print(q)

print(q.get_front())
print(q.get_end())
