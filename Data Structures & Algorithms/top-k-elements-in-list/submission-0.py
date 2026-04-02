class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}

        for x in nums: 
            if x not in vals: 
                vals [x] = 1
            else: 
                vals [x]+=1

        vals = sorted (vals.items(), key = lambda items: items [1], reverse = True)
        ret = []
        print (vals [:k])
        for val, count in vals [:k]:
            ret.append (val)

        return ret


        