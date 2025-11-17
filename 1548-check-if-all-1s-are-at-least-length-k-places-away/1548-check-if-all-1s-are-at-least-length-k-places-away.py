class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if curr == -1:
                    curr = i
                    continue
                if i-curr-1 >= k:
                    curr = i
                    continue
                return False
        
        return True
        