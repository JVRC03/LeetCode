class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.jvrc = 0

        def f(arr, curr, idx):
            self.jvrc += curr

            if idx >= len(arr):
                return
            
            for i in range(idx, len(arr)):
                f(arr, curr ^ arr[i], i+1)

        f(nums, 0, 0)
        return self.jvrc
        