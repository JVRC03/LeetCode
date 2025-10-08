class Solution:
    def successfulPairs(self, jvrc: List[int], b: List[int], k: int):
        b.sort()

        def fa(n):
            f, r = 0 , len(b)-1
            ans = 0

            while f <= r:
                mid = (f+r)//2

                if  k <= (n*b[mid]):
                    r = mid-1
                    ans = mid
                else:
                    f = mid+1
            
            if ans == 0 and b[-1] * n < k:
                return ans

            return len(b)-ans

        for i in range(len(jvrc)):
            jvrc[i] = fa(jvrc[i])
        
        return jvrc
        