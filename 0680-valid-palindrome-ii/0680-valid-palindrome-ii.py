class Solution:
    def validPalindrome(self, s: str) -> bool:
        f, r = 0, len(s)-1

        def check(s, l, h):
            while l < h:
                if s[l] == s[h]:
                    l += 1
                    h -= 1
                    continue
                return False
            
            return True

        while f < r:
            if s[f] == s[r]:
                f += 1
                r -= 1
                continue

            if (check(s, f, r-1) or check(s, f+1, r)):
                return True
            else:
                return False
        
        return True


        