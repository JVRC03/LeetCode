class Solution:
    def equalSubstring(self, s: str, t: str, k: int) -> int:
        jvrc = 0
        f, r = 0, 0
        curr = 0

        while f <= r and r < len(s):
            curr += abs(ord(t[r])-ord(s[r]))

            if curr > k:
                jvrc = max(jvrc, (r-f))
                while curr > k:
                    curr -= abs(ord(t[f])-ord(s[f]))
                    f += 1
            
            r += 1
        
        jvrc = max(jvrc, (r-f))

        return jvrc

        