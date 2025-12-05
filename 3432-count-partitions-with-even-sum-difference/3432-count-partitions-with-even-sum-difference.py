class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tot, jvrc = sum(nums), 0
        curr = 0

        for i in range(len(nums)-1):
            tot -= nums[i]
            curr += nums[i]

            if (tot-curr)%2 == 0:
                jvrc += 1
        
        return jvrc
        