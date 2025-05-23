class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = {}
        f, r = 0, 0
        curr, jvrc = 0, 0

        while f <= r and r < len(nums):
            if nums[r] not in dic:
                dic[nums[r]] = r
                curr += nums[r]
                r += 1
            else:
                jvrc = max(jvrc, curr)
                while nums[f] != nums[r]:
                    del dic[nums[f]]
                    curr -= nums[f]
                    f += 1
                curr -= nums[f]
                del dic[nums[f]]
                dic[nums[r]] = r
                curr += nums[r]
                r += 1
                f += 1
        
        jvrc = max(jvrc, curr)

        return jvrc
        