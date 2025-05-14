class Solution:
    def maximumBeauty(self, a: List[List[int]], jvrc: List[int]) -> List[int]:
        a.sort()
        curr = float('-inf')
        p = []

        def f(k):
            f, r = 0, len(a)-1
            ans = -1

            while f <= r:
                mid = (f+r)//2

                if a[mid][0] > k:
                    r = mid-1
                else:
                    ans = mid
                    f = mid+1
            
            return ans

        n = 0

        while n < len(a):
            temp = a[n][0]
            c = 0
            while True:
                if n >= len(a):
                    break

                if temp == a[n][0]:
                    curr = max(curr, a[n][1])
                    c += 1
                    n += 1
                else:
                    break

            for i in range(c):
                p.append(curr)
        
        for i in range(len(jvrc)):
            k = f(jvrc[i])

            if k == -1:
                jvrc[i] = 0
                continue
            jvrc[i] = p[k]

        return jvrc
        

        