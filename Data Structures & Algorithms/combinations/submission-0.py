class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def helper (ranges, numbers):
            if len (numbers) == k:
                ret.append (numbers.copy())
                return 
            for i in range (ranges,n+1):
                numbers.append (i)
                helper (i+1, numbers)
                numbers.pop()

        helper (1,[])
        return ret

            


            