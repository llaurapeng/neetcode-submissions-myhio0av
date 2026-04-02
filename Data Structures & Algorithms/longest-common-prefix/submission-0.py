class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minLen = float ("inf")

        for val in strs:
            minLen = min (minLen, len (val))
        #go through each string
        ret = strs [0][:minLen]
        print (ret)
        for dex, val in enumerate (strs[1:]):
            for x in range (minLen):
                #add: if 2 have the same value
                #reset: if 2 have different values
                if x < len (ret):
                    if ret [x] != val [x]:
                        ret = val [:x]
                    
        return ret






                


        