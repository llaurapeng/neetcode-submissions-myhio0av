class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(dex):
            # Base case: if we reach the end of the string, it's a valid decoding
            if dex == len(s):
                return 1
            
            # If the current digit is '0', it can't be decoded
            if s[dex] == '0':
                return 0

            # Option 1: Decode the current single digit
            count = helper(dex + 1)

            # Option 2: Decode the current and next digit if it's a valid number (10-26)
            if dex + 1 < len(s) and 10 <= int(s[dex:dex + 2]) <= 26:
                count += helper(dex + 2)

            return count

        # Start the recursion from index 0
        return helper(0)