class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len (temperatures)
        dex = 0 

        for dex, currV in enumerate (temperatures):

            while stack and currV > stack [-1][0]:
                stackValue, stackInd = stack.pop()
                ret [stackInd] = dex - stackInd

            stack.append ((currV, dex))      

        return ret





            



                    







            

