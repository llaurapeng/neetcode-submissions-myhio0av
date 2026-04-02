class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def sameSign (a,b):
            if a > 0 and b > 0:
                return True
            else:
                return False

        s = []
        for a in asteroids:
            col = False
            ab = abs (a)

            while s and s[-1] > 0 and a < 0:
                #there is an collision

                if ab > s[-1]:
                    s.pop()

                elif s[-1] == ab:
                    col = True
                    s.pop()
                    break
         
                elif s[-1] >= ab:
                    col = True
                    break

            if col == True:
                continue
            else: 
                s.append (a)

        return s                    
                
                

            

              