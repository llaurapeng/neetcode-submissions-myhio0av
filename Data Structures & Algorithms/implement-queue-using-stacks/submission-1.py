class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        '''
        2 stacks
        s1 = keep adding to s1 when pushing
        s2 = when we want to do a pop, then remove from s1 and add to s2 
        and return the top element in s2

        '''
        

    def push(self, x: int) -> None:
        self.s1.append (x)
        
    def pop(self) -> int:

        if not self.s2:
            leng = len (self.s1)

            for i in range (leng):
                val = self.s1.pop()
                self.s2.append (val)

        return self.s2.pop()

    def peek(self) -> int:

        if not self.s2:
            leng = len (self.s1)

            for i in range (leng):
                val = self.s1.pop()
                self.s2.append (val)

        return self.s2[-1]
        
    def empty(self) -> bool:
        if len (self.s1) == 0 and len (self.s2) == 0:
            return True
        else: 
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()