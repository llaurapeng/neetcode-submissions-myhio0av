class Solution:
    def isValid(self, s: str) -> bool:
        s = list (s)
        brackets = []
        open = ['{','[','(']
        closing = ['}',']',')']

        if s [0] in closing: 
            return False
        
        for val in s: 
            if brackets: 
                if val == ')':
                    if brackets [-1] == '(': 
                        brackets.pop ()
                    else: 
                        return False
                if val == '}':
                    if brackets [-1] == '{': 
                        brackets.pop ()
                    else: 
                        return False

                if val == ']':
                    if brackets [-1] == '[': 
                        brackets.pop ()
                    else: 
                        return False

            #only add opening brackets and not closing

            if val in open: 
                brackets.append (val)
            
        if len (brackets) == 0: 
            return True

        else: 
            return False

    







