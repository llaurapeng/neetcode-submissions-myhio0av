class TimeMap:

    def __init__(self):
        self.ret = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #key: [val, time]

        if key not in self.ret:
            self.ret[key] = []

        self.ret[key].append ([value, timestamp]) 

    def get(self, key: str, timestamp: int) -> str:

        # need to find the timestmp 

        if key not in self.ret: 
            return ''

        res = ''

        l,r = 0, len (self.ret [key])-1

        while l<=r: 
            mid = (l+r)//2

            if self.ret[key][mid][1] <= timestamp: 
                res = self.ret[key][mid][0]

            if self.ret[key][mid][1] > timestamp: 
                #need to look towards the left
                r = mid - 1
            else: 
                l = mid + 1
        return res

 
        
            


        
