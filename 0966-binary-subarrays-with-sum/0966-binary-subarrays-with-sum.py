class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        
        def f():
            ans = 0
            c = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    c += 1
                    continue
                ans += ((c*(c+1))//2)
                c = 0
            
            if c:
                ans += ((c*(c+1))//2)

            return ans 

        if k == 0:
            return f()
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



       