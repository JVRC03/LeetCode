class Solution:
    def maximumRemovals(self, s: str, k: str, arr: List[int]):

        def check(idx, s, k, arr):
            a = list(s)

            for i in range(idx):
                a[arr[i]] = '-'
            
            f = 0
            for i in range(len(a)):
                if f == len(k):
                    return True
                if a[i] == k[f]:
                    f += 1
                    continue
            if f == len(k):
                return True
            
            return False
                 
        f, r = 0, len(arr)
        jvrc = -1
        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, s, k, arr):
                jvrc = max(jvrc, mid)
                f = mid+1
            else:
                r = mid-1
        
        return jvrc
        