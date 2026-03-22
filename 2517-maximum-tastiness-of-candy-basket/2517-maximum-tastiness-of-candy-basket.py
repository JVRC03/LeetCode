class Solution:
    def maximumTastiness(self, arr: List[int], k: int) -> int:
        arr.sort()
        f, r = 0, max(arr)
        jvrc = float('-inf')

        def check(val, arr, k):
            last_idx = -1

            for i in range(len(arr)):
                if not k:
                    return True
                
                if last_idx == -1:
                    last_idx = arr[i]
                    k -= 1
                    continue
                
                if arr[i]-last_idx >= val:
                    last_idx = arr[i]
                    k -= 1

            if not k:
                return True
            return False

        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, arr, k):
                jvrc = max(jvrc, mid)
                f = mid+1
            else:
                r = mid-1
        
        return jvrc
        