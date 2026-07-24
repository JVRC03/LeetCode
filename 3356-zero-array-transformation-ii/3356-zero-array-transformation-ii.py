class Solution:
    def minZeroArray(self, nums: List[int], q: List[List[int]]) -> int:
        f, r = 0, len(q) - 1
        jvrc = float('inf')

        def check(n, q, nums):

            diff = [0] * len(nums)
            
            for i in range(n + 1):
                a, b = q[i][0], q[i][1]
                c = q[i][-1]

                diff[a] += c

                if b + 1 < len(diff):
                    diff[b + 1] -= c
            
            p_sum = 0
            for i in range(len(diff)):
                p_sum += diff[i]
                if nums[i] - p_sum > 0:
                    return 0
            
            return True

        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, q, nums):
                jvrc = min(jvrc, mid + 1)
                r = mid - 1
            else:
                f = mid + 1
        
        if nums.count(0) == len(nums):
            return 0
        if jvrc == float('inf'):
            return -1
        
        return jvrc
        