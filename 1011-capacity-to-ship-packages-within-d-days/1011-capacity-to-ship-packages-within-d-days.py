class Solution:
    def shipWithinDays(self, arr: List[int], k: int) -> int:
        low, high = max(arr), sum(arr)
        jvrc = float('inf')

        def check(n, arr):
            tot = 0
            curr = 0

            for i in range(len(arr)):
                if curr+arr[i] <= n:
                    curr += arr[i]
                else:
                    tot += 1
                    curr = arr[i]
            
            tot += 1
            
            return tot

        while low <= high:
            mid = low + ((high - low) // 2)
            ans = check(mid, arr)
            
            if ans <= k:
                jvrc = min(jvrc, mid)
                high = mid-1
            else:
                low = mid+1
                
        return jvrc
        