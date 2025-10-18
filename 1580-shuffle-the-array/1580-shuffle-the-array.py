class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        jvrc = []
        f, r = 0, n
        while f < r and r < len(nums):
            jvrc.append(nums[f])
            jvrc.append(nums[r])
            r += 1
            f += 1
        
        return jvrc
        