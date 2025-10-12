class Solution:
    def minimizedMaximum(self, k: int, nums: List[int]) -> int:
        f, r = 1, max(nums)
        jvrc = float('inf')

        def check(n):
            c = 0

            for i in range(len(nums)):
                if nums[i]%n == 0:
                    c += (nums[i]//n)
                else:
                    c += (nums[i]//n)
                    c += 1
            
            return c

        while f <= r:
            mid = (f+r)//2

            a = check(mid)

            if a <= k:
                r = mid-1
                jvrc = min(jvrc, mid)
            else:
                f = mid+1
                
        
        return jvrc
        