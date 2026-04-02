class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        sets = set ()
        ret = 0

        for r in range (len (s)):
            while s[r] in sets: 
                sets.remove (s[l])
                l+=1

            sets.add (s[r])

            ret = max (ret, r - l + 1)

        return ret

        