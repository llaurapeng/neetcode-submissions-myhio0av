class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set (s)
        ret = 0

        for char in chars: 
            kleft = 0 
            l = 0 
            for r, letter in enumerate (s): 
                if letter != char: 
                    while kleft >= k: 
                        if s [l] != char: 
                            kleft-=1   
                        l+=1

                    #kleft <= k
                    kleft+=1

                ret = max (ret, r - l + 1)

        return ret

                


                

                



                
