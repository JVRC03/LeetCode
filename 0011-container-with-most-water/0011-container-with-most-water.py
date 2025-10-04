class Solution:
    def maxArea(self, arr: List[int]) -> int:
        jvrc = 0
        f, r = 0, len(arr)-1

        while f < r:
            k = min(arr[f], arr[r])

            jvrc = max(jvrc, (r-f)*k)

            if arr[f] < arr[r]:
                f += 1
            else:
                r -= 1
        
        return jvrc
        