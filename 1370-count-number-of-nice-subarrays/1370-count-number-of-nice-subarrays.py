class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        f, r = 0, 0
        jvrc = 0
        c = 0
        idx = -1

        while f <= r and r < len(nums):
            if nums[r]%2 == 1:
                c += 1
            
            if c == k:
                if idx == -1:
                    idx = r
            elif c > k:
                diff = r-idx
                while c > k:
                    jvrc += diff
                    if nums[f]%2 == 1:
                        c -= 1
                    f += 1
                idx = r
            
            r += 1
        
        if c == k:
            diff = r-idx
            while c == k and f < len(nums):
                jvrc += diff
                if nums[f]%2 == 1:
                    c -= 1
                f += 1
        
        return jvrc

        