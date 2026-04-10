class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        jvrc, dic = float('inf'), {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        
        def func(arr):
            f, r = 0, 2
            if len(arr) < 3:
                return float('inf')

            curr = float('inf')

            while r < len(arr):
                k = abs(arr[f] - arr[f + 1]) + abs(arr[f] - arr[r]) + abs(arr[f+1]-arr[r])
                curr = min(curr, k)
                r += 1
                f += 1
            
            return curr

        for i in dic:
            jvrc = min(jvrc, func(dic[i]))
        
        if jvrc == float('inf'):
            jvrc = -1
        
        return jvrc

        