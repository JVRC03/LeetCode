class NumArray:

    def __init__(self, nums: list[int]):
        self.pref = [nums[0]]

        for i in range(1, len(nums)):
            self.pref.append(self.pref[-1] + nums[i])

    def sumRange(self, l: int, r: int) -> int:
        if l > 0:
            return self.pref[r] - self.pref[l - 1]
        
        return self.pref[r]
        


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)