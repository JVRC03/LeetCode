class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        arr = []

        for i in range(max(nums)+1):
            arr.append([0, 0])

        for i in range(1, len(arr)):
            c = i
            for j in range(i, len(arr), c):
                arr[j][0] += 1
                arr[j][1] += i

        jvrc = 0

        for i in range(len(nums)):
            if arr[nums[i]][0] == 4:
                jvrc += arr[nums[i]][-1]
        
        return jvrc

        