class Solution:
    def minimumIndex(self, arr: list[int], k: int) -> int:
        diff = float('inf')
        jvrc = -1
        
        for i in range(len(arr)):
            if arr[i] >= k:
                curr = abs(arr[i]-k)
                if curr < diff:
                    diff = curr
                    jvrc = i

        return jvrc
        