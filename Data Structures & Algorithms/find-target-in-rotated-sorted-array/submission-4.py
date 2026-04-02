class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l, r = 0, len (nums)-1

        while l <= r:
            m = (l + r) //2

            if nums [m] == target: 
                return m

            if nums [m] >= nums [l]:
                #in the left portion

                if target < nums [l]:
                    l = m+1

                elif target > nums [m]:
                    l = m + 1

                elif target < nums [m]:
                    r = m - 1

            else:
                #in the right portion
                if target > nums [r]:
                    r = m - 1
                elif target > nums [m]:
                    l = m + 1
                elif target < nums [m]:
                    r = m - 1

        return -1





