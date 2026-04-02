class Solution:
    def partitionLabels(self, s: str) -> List[int]:
  

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
            start = listy[0]
            end = listy [1]

            if start > prev_range [1]:
                #no conflicts
                ret.append (start - prev_range [0])
                prev_range = [start, end]

            #there is a conflict 
            #start is less than the end of the previous range
            elif start < prev_range [1]:
                prev_range = [min (start, prev_range [0]), max (end, prev_range [1])]

        ret.append (prev_range [1] - prev_range [0]+1)
        return ret            