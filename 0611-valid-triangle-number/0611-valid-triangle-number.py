class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        jvrc = 0

        for i in range(len(nums)):
            c = 0
            for j in range(i+1, len(nums)):
                f, r = j+1, len(nums)-1
                ans = -1

                while f <= r:
                    mid = (f + r) // 2

                    if nums[mid] >= nums[i]+nums[j]:
                        r = mid-1
                    else:
                        ans = mid
                        f = mid+1
                
                if ans != -1:
                    jvrc += (ans - j)
                    c += (ans - j)            

        return jvrc
        