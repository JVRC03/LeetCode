class Solution:
    def aggregateTimeSeries(self, a: list[list[int]], b: list[list[int]]):
        jvrc = []
        f, r = 0, 0

        s = set()
        for i in range(len(a)):
            s.add(a[i][0])
        for i in range(len(b)):
            s.add(b[i][0])
        
        l = list(s)
        l.sort()
        for i in range(len(l)):
            jvrc.append([l[i]])

        def check(k, arr):
            f, r = 0, len(arr) - 1
            ans = 0

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid][0] >= k:
                    r = mid - 1
                    ans = arr[mid][-1]
                else:
                    f = mid + 1
            
            return ans

        for i in range(len(jvrc)):
            x, y = check(jvrc[i][0], a), check(jvrc[i][0], b)
            jvrc[i].append(x + y)
        
        return jvrc
        