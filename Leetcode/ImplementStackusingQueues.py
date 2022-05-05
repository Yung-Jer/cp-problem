# Easiest way to implement a stack, but pop is O(n)
class MyStack(object):

    def __init__(self):
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.q.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.q) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Implementation below could make pop and top O(1)

import collections
class Stack(object):
    def __init__(self):
        self.queue = None

    def push(self, x):
        q = collections.deque()
        q.append(x)
        q.append(self.queue)
        self.queue = q

    def pop(self):
        self.queue.popleft()
        self.queue = self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue