class Solution:
    def maxIceCream(self, nums: List[int], k: int) -> int:
        arr = [0] * 100001

        for i in range(len(nums)):
            arr[nums[i]] += 1
        jvrc = 0
        for i in range(len(arr)):
            while k >= i and arr[i]:
                k -= i
                jvrc += 1
                arr[i] -= 1
        
        return jvrc

        