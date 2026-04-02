class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        


        self.ret = []

        def helper (vals):
            if len (vals) == 0: 
                return [[]]
            perms = helper (vals [1:])       
            curr_res = []
            for p in perms: 
                for i in range (len (p)+1):
                    p_copy = p.copy()
                    p_copy.insert (i, vals [0])
                    if p_copy not in curr_res: 
                        curr_res.append (p_copy)
            return curr_res

        return helper (nums)                 

                         