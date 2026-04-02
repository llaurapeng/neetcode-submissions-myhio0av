class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        if len (s) != len (t): 
            return False
        for i in range (len (s)):
            if s[i] not in sdict: 
                sdict [s[i]] = 0

            if t[i] not in tdict: 
                tdict [t[i]] = 0

            sdict [s[i]]+=1
            tdict [t[i]]+=1

        if sdict == tdict: 
            return True
        else: 
            return False
            