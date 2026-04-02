class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0 

        counter = {}
        currStart= {}

        for val in t: 
            if val not in counter: 
                counter [val] = 0 
                currStart [val] = 0
            counter [val]+=1

        curr = currStart.copy()
        ret = [float ('inf'),0]

        def equalCheck (a, b):
            for key, value in a.items():
                if b[key] < value: 
                    return False
            return True

        
        for r, val in enumerate (s):
            if val in counter: 
                curr [val]+=1

            print (curr)
            print ('---') 
            while equalCheck (counter, curr): 
                print ('this')
                #can start incrementing the left pointer
                if ret[0] > r-l: 
                    print ('answer')

                    ret [0] = r - l
                    ret [1] = s [l:r+1]
                if s [l] in curr: 
                    curr [s[l]]-=1
                l+=1
    
        return ret [1] if ret [1] != 0 else ""
            




            


            







        