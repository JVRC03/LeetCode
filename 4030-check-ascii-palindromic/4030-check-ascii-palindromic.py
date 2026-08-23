class Solution:
    def isPalindromic(self, s: str) -> bool:

        f, r = 0, len(s) - 1

        while f <= r:
            a = bin(ord(s[f]))
            a = a[2:]

            b = bin(ord(s[r]))
            b = b[2:]

            a = ('0' * (8 - len(a))) + a
            b = ('0' * (8 - len(b))) + b

            i = 0
            while i < 8:
                if a[i] != b[-i-1]:
                    return False
                i += 1
            
            f += 1
            r -= 1
        
        return True

        