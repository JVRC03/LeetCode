class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        act_sum, tot_sum = 0, (n * (n + 1)) // 2
        act_sq, sq = 0, 0

        for i in range(len(nums)):
            act_sum += nums[i]

            act_sq += (nums[i] ** 2)
            sq += ((i + 1) ** 2)
        
        a_b = tot_sum - act_sum
        a2_b2 = sq - act_sq

        aPb = a2_b2 // a_b
        a = (aPb + a_b) // 2

        b = aPb - a

        return [b, a]


        

        
        