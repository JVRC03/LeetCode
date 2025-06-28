class Solution:
    def maxSubsequence(self, jvrc: List[int], k: int) -> List[int]:
        arr = jvrc.copy()
        jvrc.sort()
        dic = {}

        while k:
            k -= 1
            if jvrc[-1] not in dic:
                dic[jvrc[-1]] = 1
            else:
                dic[jvrc[-1]] += 1
            jvrc.pop()

        jvrc = []

        for i in range(len(arr)):
            if arr[i] in dic and dic[arr[i]] > 0:
                dic[arr[i]] -= 1
                jvrc.append(arr[i])

        return jvrc
        