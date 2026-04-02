class Solution:
    def jump(self, nums: List[int]) -> int:
        goalDex = len (nums)-1
        ret = 0 
        found = False

        while goalDex != 0: 
            newGoal = -1
            for beforeDex in range (goalDex-1, -1, -1):
                if beforeDex + nums [beforeDex] >= goalDex:
                    newGoal = beforeDex
                    found = True

            if found is True: 
                ret+=1
                found = False

            goalDex = newGoal

        return ret

