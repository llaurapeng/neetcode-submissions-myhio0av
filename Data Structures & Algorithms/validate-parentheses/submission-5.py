class Solution:
    def isValid(self, s: str) -> bool:

        #store all the opening brackets in one stack
        #get rid of elements in the stack if it is a closing bracket
        closeOpen ={'{':'}', '[':']','(': ')'}
        stacky = []

        for x in s: 
            #if the current is not a ending bracket
            if x in closeOpen.keys(): 
                print ('open')
                print (x)
                stacky.append(x)
                print ('---')
            
            #if the current is a ending bracket and the right one for the stack
            elif stacky and x == closeOpen [stacky[len (stacky)-1]]: 
                print ('close')
                print (x)
                stacky.pop (len (stacky)-1)

            else: 
                return False

        if len (stacky) == 0: 
            return True
       
        return False

            

            