class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+','-','*','/']
        total = 0

        if len (tokens)== 1:
            return int (tokens [0])
            
        for x in tokens:
            if x in ops: 
                firstVal = int (stack.pop())
                secondVal = int (stack.pop())
                if x == "+": 
                    val = firstVal + secondVal

                if x == '-':
                    val = secondVal - firstVal

                if x == '*':
                    val = firstVal * secondVal

                if x == '/': 
                    val = int(secondVal / firstVal)
                
                stack.append (val)

            else: 
                stack.append (x)

        return stack [0]
                


