class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for ind, num in enumerate (nums): 
            if num > 0: 
                break

            l = ind + 1
            r = len (nums)-1

            if ind != 0 and num == nums [ind-1]: 
                continue

            while l < r: 
                summ = num + nums [l] + nums [r]

                if summ > 0: 
                    #need smaller values
                    r-=1
                elif summ < 0: 
                    l+=1
                else: 
                    ret.append ([num, nums [l], nums [r]])
                    l+=1
                    r -= 1
                    while l < r and nums [l] == nums [l-1]:
                        l+=1
        return ret
                    
                    



            