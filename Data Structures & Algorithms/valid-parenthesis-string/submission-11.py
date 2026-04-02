class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMax = 0 
        leftMin = 0

        for val in s: 
            if val == "(":
                leftMax+=1
                leftMin+=1
            elif val == ")":
                leftMax-=1
                leftMin-=1
            else:
                leftMax+=1
                leftMin-=1

            if leftMax < 0: 
                return False
            
            if leftMin <0: 
                leftMin = 0

        if leftMin == 0 or leftMax == 0: 
            return True
        else: 
            return False