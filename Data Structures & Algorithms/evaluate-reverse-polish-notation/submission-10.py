class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        ret = 0

        if len (tokens) == 1: 
            return int (tokens [0])
        for x in tokens: 
            if x == "+":
                first = values.pop ()
                second = values.pop ()
                ret = int (first) + int (second)
                print (ret)
                values.append (ret)

            elif x == "-":
                first = values.pop ()

                second = values.pop ()

                ret = int (second) - int (first)
                print (ret)
                values.append (ret)
            
            elif x == "*":
                first = values.pop ()
                second = values.pop ()
                ret = int (first) * int (second)
                print (ret)
                values.append (ret)

            elif x == "/":
                first = values.pop ()
                second = values.pop ()
                ret = int (second) / int (first)
                print (ret)
                values.append (ret)

            #if number then add to values
            else: 
                values.append (x)
        return int (ret)


        