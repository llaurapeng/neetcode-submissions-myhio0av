class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        ret = [0] * len (temperatures)
        s = []


        for ind, temp in enumerate (temperatures): 

            while s and temp > s [-1][1]:
                oldind, oldtemp = s.pop()
                ret [oldind] = ind - oldind

            s.append ([ind, temp])


        return ret
                


                




            