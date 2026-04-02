class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l, r = 0, 0
        ret = ''


        while l < len (word1) and r < len (word2):
            ret+= word1[l] + word2[r]
            l+=1
            r+=1

        if l < len (word1):
            ret+= word1[l:]
        elif r < len (word2): 
            ret+= word2[r:]
       
        return ret
