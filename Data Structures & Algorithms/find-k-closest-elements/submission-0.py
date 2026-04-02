class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        [4,2,1,4]
        -deduct each from x


        '''

        deduct = []

        for num in arr: 
            deduct.append ([abs (num - x), num])

        deduct.sort ()
        ret = []

        print (deduct)
        for ind in range (k):
            ret.append (deduct [ind][1])

        ret.sort()
        return ret

