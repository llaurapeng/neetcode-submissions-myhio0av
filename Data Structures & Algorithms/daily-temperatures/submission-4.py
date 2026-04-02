class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        l = 0 
        r = 1   
        ret = []

        for l in range (len (temperatures)):
            curr = temperatures [l]
            num = 0
            found = False
            for r in range (l, len (temperatures)):
                if temperatures[r] > curr: 
                    found = True
                    break

                num+=1

            if found is True:
                ret.append (num)
            else:
                ret.append (0)
        return ret







