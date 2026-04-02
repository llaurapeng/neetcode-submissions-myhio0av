class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def helper (startDex, values):

            if len (values) == len (digits):
                res.append (values)
                return
            for x in digitToChar [digits[startDex]]:
                helper (startDex+1, values + x)

        if digits: 
            helper (0, '')

        return res

        