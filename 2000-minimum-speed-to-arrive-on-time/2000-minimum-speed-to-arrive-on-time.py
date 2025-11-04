class Solution:
    def minSpeedOnTime(self, arr: List[int], k: float) -> int:
        if len(arr)-1 > k:
            return -1
        
        f, r = 1, 10000000
        jvrc = float('inf')

        def check(n):
            ans = 0
            for i in range(len(arr)-1):
                ans += (int(math.ceil(arr[i]/n)))
            
            ans += (arr[-1]/n)

            return ans

        while f <= r:
            mid = (f + r)//2
            c = check(mid)

            if c <= k:
                r = mid-1
                jvrc = min(jvrc, mid)
            else:
                f = mid+1
        
        if jvrc == float('inf'):
            return -1
        return jvrc







        