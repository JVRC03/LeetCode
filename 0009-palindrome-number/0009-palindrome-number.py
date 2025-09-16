class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        s = s[::-1]

        if int(s) == x:
            return True
        
        return False
        