class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal (val):
            reverse = val[::-1]
            if val == reverse: 
                return True
            else: 
                return False

        ret = 0
        
        #will store the number of different palindromes from 1 to index i
        for ind in range (len (s)):
            ret+=1
            for afterdex in range (ind+1,len (s)):
                if isPal (s [ind:afterdex+1]):
                    ret+=1
                else:
                    continue

        return ret
