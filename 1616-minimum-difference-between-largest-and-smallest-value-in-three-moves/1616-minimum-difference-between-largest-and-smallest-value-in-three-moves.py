class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        
        nums.sort()

        def f(arr):
            jvrc = float('inf')

            jvrc = min(jvrc, abs(arr[0]-arr[-1]))
            jvrc = min(jvrc, abs(arr[0]-arr[-2]))
            jvrc = min(jvrc, abs(arr[0]-arr[-3]))
            jvrc = min(jvrc, abs(arr[0]-arr[-4]))

            jvrc = min(jvrc, abs(arr[1]-arr[-1]))
            jvrc = min(jvrc, abs(arr[1]-arr[-2]))
            jvrc = min(jvrc, abs(arr[1]-arr[-3]))

            jvrc = min(jvrc, abs(arr[2]-arr[-1]))
            jvrc = min(jvrc, abs(arr[2]-arr[-2]))

            jvrc = min(jvrc, abs(arr[3]-arr[-1]))

            return jvrc

        return min(f(nums), f(nums[::-1]))

        