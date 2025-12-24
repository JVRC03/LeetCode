class Solution:
    def countRectangles(self, arr: List[List[int]], jvrc: List[List[int]]):
        arr.sort()
        dic = {}
        temp = [0] * 101

        for i in range(len(arr)-1, -1, -1):
            temp[arr[i][-1]] += 1
            dic[i] = temp.copy()
            
        def fa(k):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = (f + r)//2

                if arr[mid][0] >= k:
                    r = mid-1
                    ans = mid
                else:
                    f = mid+1
            
            return ans

        def fb(start, k):
            ans = 0
            temp = dic[start]

            for i in range(len(temp)):
                if i >= k:
                    ans += temp[i]

            return ans

        for i in range(len(jvrc)):
            x = fa(jvrc[i][0])
            if x == -1:
                jvrc[i] = 0
                continue
            y = fb(x, jvrc[i][-1])

            jvrc[i] = y
        
        return jvrc

        