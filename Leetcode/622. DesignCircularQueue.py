class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * (k + 1)
        self.front = 0
        self.back = 0
        self.MAX_SIZE = k

    def enQueue(self, value: int) -> bool:
        if (self.back + 1) % (self.MAX_SIZE + 1) == self.front:
            return False
        self.queue[self.back] = value
        self.back = (self.back + 1) % (self.MAX_SIZE + 1)
        return True

    def deQueue(self) -> bool:
        if self.back == self.front:
            return False
        self.front = (self.front + 1) % (self.MAX_SIZE + 1)
        return True

    def Front(self) -> int:
        return self.queue[self.front] if self.front != self.back else -1

    def Rear(self) -> int:
        return self.queue[self.back - 1] if self.front != self.back else -1
        

    def isEmpty(self) -> bool:
        return self.front == self.back

    def isFull(self) -> bool:
        return (self.back + 1) % (self.MAX_SIZE + 1) == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()