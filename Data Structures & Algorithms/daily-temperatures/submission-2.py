class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []

        ret = [0] * len (temperatures)

        for ind, temp in enumerate (temperatures): 
            while temps and int (temps[-1][0]) < int (temp): 
                # if the curr temp is greater than the top of the stack
                    prevIndex = temps [-1][1]

                    ret [prevIndex] = ind - prevIndex

                    temps.pop()

            temps.append ([temp, ind])

        return ret

                




            



                    







            

