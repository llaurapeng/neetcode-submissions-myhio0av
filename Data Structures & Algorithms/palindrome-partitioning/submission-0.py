class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def isPal (a, b):
            while a < b: 
                if s[a]!= s[b]:
                    return False
                a, b = a+ 1, b-1

            return True
        def helper (i, res):

            if i >= len (s):
                ret.append (res.copy())
                return 

            for dex in range (i, len (s)):
                if isPal (i, dex):
                    #start exploring
                    res.append (s[i:dex+1])
                    helper (dex+1, res)
                    res.pop()

        helper (0, [])

        return ret




