class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valCount = {}

        for val in nums: 
            if val in valCount: 
                valCount [val]+=1
            else: 
                valCount [val] = 1

        
        #return the key sorted by increasing key values and return first k

        ret = [key for key, value in sorted (valCount.items(), key = lambda item: item [1], reverse = True)]

        return ret [:k]