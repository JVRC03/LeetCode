class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        arr = []
        a, b = 0, 1
        c = a+b
        jvrc = 0

        while c <= k:
            arr.append(c)
            a = b
            b = c
            c = a+b

        def fa(x):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = (f+r)//2

                if arr[mid] > x:
                    r = mid-1
                else:
                    ans = arr[mid]
                    f = mid+1
            
            return ans

        while k > 0:
            a = fa(k)
            if a == -1:
                k -= arr[-1]
                jvrc += 1
                continue
            k -= a
            jvrc += 1
        

        return jvrc