class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        vals = list(set(list(s)))

        def func(s, char, k):
            ans = 0
            f, r = 0, 0
            curr = 0

            while f <= r and r < len(s):
                if s[r] == char:
                    curr += 1
                else:
                    if k:
                        curr += 1
                        k -= 1
                    else:
                        while s[f] == char:
                            f += 1
                            curr -= 1
                        f += 1
                        
                r += 1

                ans = max(ans, curr)
            
            return ans
                
        jvrc = 0
        for i in range(len(vals)):
            jvrc = max(jvrc, func(s, vals[i], k))
        
        return jvrc
        