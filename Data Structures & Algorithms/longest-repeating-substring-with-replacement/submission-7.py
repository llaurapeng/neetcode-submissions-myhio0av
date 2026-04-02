class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0

        char = set (s)

        for c in char: 
            l = 0 
            currk = 0 
            for r in range (len (s)):
                if s[r] != c:
                    currk+=1

                while currk > k: 
                    if l < len (s) and c != s[l]:
                        currk-=1
                    l+=1

                ret = max (ret, (r-l)+1)

        return ret


            


        