class MyQueue:

    #first in, first out
    #stack: last, first out

    def __init__(self):
        self.que = []
        self.que2 = []

    def push(self, x: int) -> None:
        self.que.append (x)
    def pop(self) -> int:
        '''
        -take everything out of que and put into que2
        -the last element in que2 should be popped

        *Need to be specific about when things are moved into the other
        -only move if the second q is empty
        '''
        if not self.que2:
            while self.que:
                val = self.que.pop()
                self.que2.append (val)

        val = self.que2.pop()

        return val

    def peek(self) -> int:
        if not self.que2:
            while self.que:
                val = self.que.pop()
                self.que2.append (val)

        val = self.que2[-1]

        return val

    def empty(self) -> bool:
        if len (self.que) == 0 and len (self.que2) == 0:
            return True
        else: 
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()