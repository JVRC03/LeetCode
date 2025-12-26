class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        jvrc = 0
        f, r = 0, 0

        def dfs(n, target):
            a, b = 0, n
            ans = -1

            while a <= b:
                mid = (a + b) // 2

                if nums[mid]+k >= target:
                    ans = mid
                    b = mid-1
                else:
                    a = mid+1
            
            return ans
        
        while f <= r and r < len(nums):

            if nums[r]-k <= nums[f]+k:
                r += 1
                continue
            
            x = dfs(f-1, nums[r-1]-k)

            if x == -1:
                x = f
            
            z = f-x
            tot = (r - f) + z

            jvrc = max(jvrc, tot)

            f += 1
        
        x = dfs(f-1, nums[r-1]-k)
        if x == -1:
            x = f
        
        z = f-x
        tot = (r - f) + z

        jvrc = max(jvrc, tot)
        
        return jvrc



       