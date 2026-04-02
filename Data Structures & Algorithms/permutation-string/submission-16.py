class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #store a maping of how many characters are in s1

        s1Count = {}

        for s in list (s1):
            if s not in s1Count: 
                s1Count [s] = 1
            else: 
                s1Count [s]+=1
        l = 0 

        og = s1Count.copy()

        r = 0

        while r < len (s2):
            if s2[r] not in s1Count: 
                l = r
                s1Count = og.copy()

            elif s1Count[s2[r]] == 0: 
                print (s2[r])
                while s1Count[s2[r]] == 0: 
                    if s2[l] in s1Count:
                        s1Count [s2[l]] +=1
                    l+=1

                s1Count [s2[r]] -=1

                print (s1Count)

            elif s2[r] in s1Count: 
                s1Count [s2[r]] -=1

            r+=1

            end = 0
            for key, value in s1Count.items():
                if value == 0: 
                    end+=1

            if end == len (s1Count): 
                return True

            

        return False


        
