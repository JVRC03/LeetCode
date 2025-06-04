class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        if len(arr) == k:
            return sum(arr)
        
        jvrc = 0
        curr, r = 0, 1

        for i in range(k):
            curr += arr[i]
        
        jvrc = max(jvrc, curr)
        while k-1 >= 0:
            curr -= arr[k-1]
            k -= 1
            curr += arr[-r]
            r += 1
            jvrc = max(jvrc, curr)
        
        return jvrc




        