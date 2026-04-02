class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        #values at later positions are processed first
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s) # this new value is at -1
            
            if len (stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop ()

        return len (stack)


        