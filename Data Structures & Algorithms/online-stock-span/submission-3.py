class StockSpanner:

    def __init__(self):
        self.prices = []
        self.s = []
        

    def next(self, price: int) -> int:
        
        #decreasing stack
        '''
        -anytime we have a increasing value
        --> we need to pop frm the end of the stack
        --> keep popping until it is decreasing
        '''
        ret = 1
        while self.s and price >= self.s[-1][1]:
            span, val = self.s.pop()
            ret+=span

        self.s.append ([ret, price])

        return ret








        

        

        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)