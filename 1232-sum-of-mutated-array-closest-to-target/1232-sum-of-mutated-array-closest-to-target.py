class Solution:
    def findBestValue(self, arr: List[int], k: int) -> int:
        arr.sort()
        f, r = 0, arr[-1]

        p_sum = [arr[0]]

        for i in range(1, len(arr)):
            p_sum.append(p_sum[-1]+arr[i])
        
        def fa(x):
            a, b = 0, len(arr)-1
            ans = -1
            while a <= b:
                mid = (a+b)//2

                if arr[mid] > x:
                    b = mid-1
                    ans = mid
                else:
                    a = mid+1

            return ans

        act, jvrc = float('inf'), float('inf')

        while f <= r:
            mid = (f+r)//2
            n = fa(mid)
            
            curr = 0
            if n > 0:
                curr = p_sum[n-1]
                curr += ((len(arr)-n)*mid)
            else:
                if mid >= arr[-1]:
                    curr = p_sum[-1]
                else:
                    curr = mid*len(arr)

            if curr > k:
                r -= 1
            else:
                f += 1

            if act > abs(curr-k):
                jvrc = mid
                act = abs(curr-k)
            elif act == abs(curr-k):
                jvrc = min(jvrc, mid)
        
        return jvrc
            
        