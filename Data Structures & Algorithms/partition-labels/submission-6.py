class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}


        for val in s: 
            if val not in counter: 
                counter [val] = 0 
            
            counter[val]+=1

        lastDex = {}

        for val in set (s): 
            if val not in lastDex:
                lastDex [val] = 0
            lastDex [val] = [s.index (val),s.rfind (val)]

        sorted_items = sorted(lastDex.items(), key=lambda x: x[1][0])
        print (sorted_items)
        ret = []
        prev_range = sorted_items [0][1]

        for key, listy in sorted_items:
            startV = listy [0]
            endV = listy [1]

            if startV <= prev_range [1] and startV >= prev_range [0]:
                prev_range[1] =max( prev_range[1],endV) 
                prev_range [0] = min (prev_range [0], startV)
            else:
                #if not within the interval
                print (key)
                ret.append (prev_range [1] - prev_range [0]+1)
                prev_range = [startV, endV]
        
        ret.append (prev_range [1] - prev_range [0]+1)
        return ret







                    
                
