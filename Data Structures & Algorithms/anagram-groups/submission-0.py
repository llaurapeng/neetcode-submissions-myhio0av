class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}

        for val in strs: 
            sorted = list(val)
            sorted.sort ()
         
            sortedStr = ''.join (sorted)

            if sortedStr in ret: 
                ret [sortedStr].append (val)
            else: 
                ret [sortedStr] = [val]

        print (list (ret.values()))
        return list (ret.values())
        
        