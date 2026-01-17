class Solution:
    def minimumTime(self, arr: List[int], k: int) -> int:
        low, high = 1, max(arr) * 10000009
        jvrc = float('inf')

        def check(arr, n):
            tot = 0

            for i in range(len(arr)):
                tot += (n//arr[i])
            
            return tot

        while low <= high:
            mid = low + ((high - low) // 2)

            ans = check(arr, mid)

            if ans >= k:
                jvrc = min(jvrc, mid)
                high = mid-1
            else:
                low = mid+1

        return jvrc
        