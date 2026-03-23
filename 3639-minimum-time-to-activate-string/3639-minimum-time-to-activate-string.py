class Solution:
    def minTime(self, s: str, arr: List[int], k: int) -> int:
        f, r = 0, len(s)
        jvrc = float('inf')

        def check(idx, arr, k):
            tot = 0
            vis = [0] * len(arr)

            for i in range(idx):
                vis[arr[i]] = 1
            
            temp = []
            for i in range(len(vis)):
                if vis[i]:
                    temp.append(i)

            for i in range(idx):
                if i == 0:
                    left, right = temp[i]+1, len(arr)-temp[i]
                    tot += (left * right)
                else:
                    left, right = (temp[i] - temp[i-1]), len(arr) - temp[i]
                    tot += (left * right)
            
            if tot >= k:
                return 1
            
            return 0

        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, arr, k):
                jvrc = min(jvrc, mid)
                r = mid-1
            else:
                f = mid+1
        
        if jvrc == float('inf'):
            return -1
        
        return jvrc-1
        