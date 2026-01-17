class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        if m*k > len(arr):
            return -1

        jvrc = float('inf')
        low, high = arr[0], arr[0]

        for i in range(len(arr)):
            low = min(low, arr[i])
            high = max(high, arr[i])
        
        def check(n, arr, kk):
            tot, c = 0, 0

            for i in range(len(arr)):
                if arr[i] <= n:
                    c += 1
                    continue
                
                tot += (c//kk)
                c = 0
            tot += (c//kk)
            return tot
        
        while low <= high:
            mid = low + ((high - low) // 2)

            ans = check(mid, arr, k)
            
            if ans < m :
                low = mid+1
            else:
                jvrc = min(jvrc, mid)
                high = mid-1
        
        return jvrc