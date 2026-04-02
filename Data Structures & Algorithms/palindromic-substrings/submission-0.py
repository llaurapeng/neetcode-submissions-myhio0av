class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal (val):
            reverse = val[::-1]
            if val == reverse: 
                return True
            else: 
                return False
        
        #will store the number of different palindromes from 1 to index i
        dp = [1] * len (s)

        for dex, val in enumerate (s): 
            print (dex)
            for beforedex in range (dex):
                #check if adding this new dex forms a new palindrome
                if isPal (s[beforedex: dex+1]):
                    print (s[beforedex: dex+1])
                    #forms a pal 
                    dp[dex] +=1
        print ('----')
        print (dp)
        return sum (dp)




        

       