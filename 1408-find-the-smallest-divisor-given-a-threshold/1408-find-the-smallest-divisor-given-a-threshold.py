class Solution:
    def smallestDivisor(self, nums: List[int], k: int) -> int:
        jvrc = float('inf')

        def fe(x):
            s = 0
  
            for i in range(len(nums)):
                g = math.ceil(nums[i]/x)
                s += g
            
            return s
        
        f, r = 1, max(nums)

        while f <= r:
            mid = math.ceil((f+r)/2)
            a = fe(mid)

            if a <= k:
                jvrc = min(jvrc, mid)
                r = mid-1
            else:
                f = mid+1
        
        return jvrc
        