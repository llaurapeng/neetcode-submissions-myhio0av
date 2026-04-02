class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         #dp [i] = if frm index i can be broken and matched starting from index i
        
        #add 1 for base case
        dp  = [False] * (len (s)+1)

        #base case
        dp [len (s)] = True

        for i in range (len (s)-1,-1,-1):
            for w in wordDict: 
                if (i + len (w)) <= len (s) and s[i : i+len (w)] == w:
                    dp [i] = dp [i + len (w)]

                if dp [i]:
                    break

        return dp [0]
        


