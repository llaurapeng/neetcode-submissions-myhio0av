class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalDex = len (nums)-1

        for dex in range (goalDex-1, -1, -1):
            dexNeeded = goalDex - dex

            if dexNeeded <= nums [dex]:
                goalDex = dex


        if goalDex != 0: 
            return False
        else: 
            return True        