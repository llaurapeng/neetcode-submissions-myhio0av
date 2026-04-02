class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len (temperatures)
        
        ret = [0] *n

        for i in range (len (temperatures)-2, -1, -1):
            currT = temperatures[i]
            dex = i + 1
            
            while dex < len (temperatures) and currT >= temperatures [dex]:
                if ret [dex] == 0:
                    dex = n
                    #nothing found
                    break
                    
                dex += ret [dex]

            if dex != n:
                ret [i] = dex - i


        return ret
