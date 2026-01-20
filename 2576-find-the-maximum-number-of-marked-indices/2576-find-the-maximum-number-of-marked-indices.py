class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        f, r = 0, 0
        a, b = nums[:len(nums)//2], nums[len(nums)//2:]

        jvrc = 0

        while f < len(a) and r < len(b):
            if 2*a[f] <= b[r]:
                f += 1
                r += 1
                jvrc += 2
            else:
                r += 1
        
        if f < len(a):

            arr = a[f:]
            i, j = len(arr)-1, len(arr)-1
            vis = [0] * len(arr)

            while i >= 0 and j >= 0:
                while j >= 0 and vis[j] == 1:
                    j -= 1
                
                k = 2*arr[i]
                if k <= arr[j]:
                    vis[j] = 1
                    vis[i] = 1
                    j -= 1
                    i -= 1
                else:
                    i -= 1

            jvrc += (vis.count(1))
        elif r < len(b):

            arr = b[r:]
            i, j = len(arr)-1, len(arr)-1
            vis = [0] * len(arr)

            while i >= 0 and j >= 0:
                while j >= 0 and vis[j] == 1:
                    j -= 1
                
                k = 2*arr[i]
                if k <= arr[j]:
                    vis[j] = 1
                    vis[i] = 1
                    j -= 1
                    i -= 1
                else:
                    i -= 1

            jvrc += (vis.count(1))

        return jvrc
            
        