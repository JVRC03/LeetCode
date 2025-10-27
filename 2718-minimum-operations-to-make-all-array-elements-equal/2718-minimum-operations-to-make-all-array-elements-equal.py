class Solution:
    def minOperations(self, nums: List[int], jvrc: List[int]) -> List[int]:
        nums.sort()
        p_sum = [nums[0]]

        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1] + nums[i])

        def naa_istam(k):
            f, r = 0, len(nums)-1
            ans, idx = 0, -1

            while f <= r:
                mid = (f + r)//2

                if nums[mid] <= k:
                    f = mid+1
                else:
                    idx = mid
                    r = mid-1

            if idx < 1:
                return abs((k * len(nums))-p_sum[-1])

            x = p_sum[idx-1]
            ans = abs((k * idx)-x)
            
            rem = len(nums)-idx
            
            ans += abs((rem*k) - (p_sum[-1]-p_sum[idx-1]))
            
            return ans

        for i in range(len(jvrc)):
            jvrc[i] = naa_istam(jvrc[i])
        
        return jvrc
        