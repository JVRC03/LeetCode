class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [[nums[-1], len(nums)-1]]
        jvrc = 0

        def f(n, arr, idx):
            f, r = 0, len(arr)-1
            ans = float('inf')

            while f <= r:
                mid = (f + r)//2

                if arr[mid][0] >= n:
                    r = mid-1
                    ans = mid
                else:
                    f = mid+1
            
            return abs(idx-arr[ans][-1])

        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= stack[-1][0]:
                jvrc = max(jvrc, f(nums[i], stack, i))
                continue
            
            stack.append([nums[i], i])
        
        return jvrc
        
        
        




        