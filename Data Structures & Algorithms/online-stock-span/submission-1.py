class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        ret = 1

        if not self.prices:
            self.prices.append (price)
            return 1

        for num in self.prices[::-1]:
            if num <= price: 
                ret+=1
            else: 
                self.prices.append (price)
                return ret

        self.prices.append (price)
        return ret

        

        

        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)