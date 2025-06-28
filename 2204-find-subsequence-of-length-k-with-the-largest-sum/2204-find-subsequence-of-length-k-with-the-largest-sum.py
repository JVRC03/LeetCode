class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = nums.copy()
        nums.sort()
        jvrc = []
        dic = {}
        c = 0

        while k:
            k -= 1
            if nums[-1-c] not in dic:
                dic[nums[-1-c]] = 1
            else:
                dic[nums[-1-c]] += 1

            c += 1
        
        for i in range(len(arr)):
            if arr[i] in dic and dic[arr[i]] > 0:
                dic[arr[i]] -= 1
                jvrc.append(arr[i])

        return jvrc
        