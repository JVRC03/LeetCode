class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        def func(arr):
            curr, c = -1, 0
            jvrc = 0

            for i in range(len(arr)):
                if arr[i] > curr:
                    curr = arr[i]
                    c += 1
                else:
                    curr = arr[i]
                    c = 1
                
                jvrc = max(jvrc, c)

            return jvrc

        return max(func(nums), func(nums[::-1]))
        