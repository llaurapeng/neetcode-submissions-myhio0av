class Solution:
    def validPalindrome(self, s: str) -> bool:
        backward = s [::-1]
        
        if backward != s: 
            leng = len (s)
            diff = 0 

            for ind in range (leng):
                news = s [:ind] + s [ind+1:]

                if news == news[::-1]:
                    return True
            return False

        else: 
            return True

