class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.ret = False

        def dp(dex):
          
            if dex == len(nums) - 1:
                self.ret = True
                return

            if dex >= len(nums) or nums[dex] == 0:
                return

            # Start from the next positions you can jump to
            for i in range(1, nums[dex] + 1):
                dp(dex + i)
                if self.ret:  # If ret is True, no need to continue
                    return

        dp(0)
        return self.ret

        