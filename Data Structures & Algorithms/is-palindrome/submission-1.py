class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        s = ''.join([val for val in s if val.isalnum()])
        
        # Convert string to lowercase
        s = s.lower()
        
        # Check if the string is equal to its reverse
        return s == s[::-1]
        