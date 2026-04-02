class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.ret = []
        self.values = []

        def helper (openC, endC): 
      
            #what is the base case

            #base #1: no more available open brackets

            if openC == endC == n: 
                self.ret.append ("".join(self.values))
                return 

            if openC < n: 
                self.values.append ('(')
                helper (openC+1, endC)
                self.values.pop()

            if endC < openC: 
                self.values.append (')')
                helper (openC, endC+1)
                self.values.pop()


            
        helper (0,0)
        return self.ret



            

            
            

