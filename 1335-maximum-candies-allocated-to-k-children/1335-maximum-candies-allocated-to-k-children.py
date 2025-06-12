class Solution:
    def maximumCandies(self, arr: List[int], k: int) -> int:
        jvrc = 0

        def fe(a):
            x = 0

            for i in range(len(arr)):
                x += (arr[i]//a)
                if x >= k:
                    return True
            
            return False
        
        f, r = 1, max(arr)

        while f <= r:
            mid = (f+r)//2

            if fe(mid):
                f = mid+1
                jvrc = max(jvrc, mid)
            else:
                r = mid-1
        
        return jvrc