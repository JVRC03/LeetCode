class Solution:
    def maxDistance(self, arr: List[int], m: int) -> int:
        arr.sort()
        f, r = 0, arr[-1]
        jvrc = 0

        def check(mid, k, arr):
            last_idx = -1

            for i in range(len(arr)):
                if not k:
                    return True
                
                if last_idx == -1:
                    k -= 1
                    last_idx = arr[i]
                    continue
                
                if arr[i]-last_idx >= mid:
                    k -= 1
                    last_idx = arr[i]
            
            if not k:
                return True
            
            return False

        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, m, arr):
                jvrc = max(jvrc, mid)
                f = mid+1
            else:
                r = mid-1
        
        return jvrc

        

        