class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        f, r = 0, 0
        jvrc = 0
        c, curr = 0, 0

        while f <= r and r < len(nums):
            if nums[r] == 1:
                c += 1
                r += 1
            elif curr < k:
                c += 1
                curr += 1
                r += 1
            else:
                jvrc = max(jvrc, c)
                
                while True:
                    if nums[f] == 0:
                        if f == r:
                            r += 1
                        f += 1
                        if c:
                            c -= 1
                        if curr:
                            curr -= 1
                        break
                    else:
                        if c:
                            c -= 1
                    f += 1
                
                
        jvrc = max(jvrc, c)

        return jvrc


           




        