import collections

class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1
    def enQueue(self, val: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.maxSize
        self.data[self.tail] = val
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail: self.head, self.tail = 0, -1
        else: self.head = (self.head + 1) % self.maxSize
        return True
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]
    def isEmpty(self) -> bool:
        return self.tail == -1
    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head

class MyCircularQueue2:
    def __init__(self, k: int):
        self.deque = collections.deque()
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1] 

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.k