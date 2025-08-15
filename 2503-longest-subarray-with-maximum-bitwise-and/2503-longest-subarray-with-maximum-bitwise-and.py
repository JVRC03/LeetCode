class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        idx = nums.index(max(nums))
        curr, prev = nums[idx], nums[idx]
        val = nums[idx]
        jvrc = 0

        for i in range(idx):
            nums[i]=-1

        while True:
            r = 0
            k = nums[idx]
            for i in range(idx, len(nums)):
                curr = curr&nums[i]

                if curr < prev or nums[i] != k:
                    curr = prev
                    break
                nums[i] = -1
                prev = curr
                r += 1
            
            jvrc = max(jvrc, r)

            idx = nums.index(max(nums))
            curr, prev = nums[idx], nums[idx]
            if nums[idx] != val:
                break
            if idx == 0:
                break
        
        return jvrc

        