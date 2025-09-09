class Solution:
    def minEatingSpeed(self, arr: List[int], k: int) -> int:
        jvrc = float('inf')

        def mine(a, b):
            c = 0

            for i in range(len(arr)):
                c += (math.ceil(arr[i]/a))
            
            if c <= b:
                return 1
            
            return 0
        
        f, r = 1, max(arr)

        while f <= r :
            mid = (f+r)//2

            if mine(mid, k):
                jvrc = min(jvrc, mid)
                r = mid-1
            else:
                f = mid+1
            
        return jvrc
            

        