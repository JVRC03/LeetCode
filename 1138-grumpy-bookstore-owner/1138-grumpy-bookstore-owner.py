class Solution:
    def maxSatisfied(self, arr: List[int], g: List[int], k: int) -> int:
        jvrc = 0
    
        for i in range(len(arr)):
            if g[i] == 0:
                jvrc += arr[i]
        
        curr = 0

        for i in range(k):
            if g[i] == 1:
                curr += arr[i]
        glob_max = curr
        f = 0
        for i in range(k, len(arr)):
            if g[i] == 1:
                curr += arr[i]
            if g[f] == 1:
                curr -= arr[f]
            f += 1
            glob_max = max(glob_max, curr)

        
        return jvrc+glob_max
            


        