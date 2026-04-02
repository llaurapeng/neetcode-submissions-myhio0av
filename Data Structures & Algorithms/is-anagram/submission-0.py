class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        contain1 = {}

        for x in s: 
            if x not in contain1: 
                contain1[x] = 0 

            contain1[x]+=1

        contain2 = {}

        for x in t: 
            if x not in contain2: 
                contain2[x] = 0 

            contain2[x]+=1

        print (contain1)
        print (contain2)

        return contain1 == contain2

        