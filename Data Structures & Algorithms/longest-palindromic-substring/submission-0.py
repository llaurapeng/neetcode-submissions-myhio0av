class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal (stri):
            reverse = stri [::-1]

            if stri == reverse: 
                return True
            else: 
                return False

        dp = list (s)

        for i in range (1,len (s)):
            for j in range (0,i):
            
                if isPal (s[j:i+1]):
                    if len (dp[j:i+1]) > len (dp[i]):

                        dp [i] = s[j:i+1]
                    
                #doesn't include index i

        return max(dp, key=len)

        
