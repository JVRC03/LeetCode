class Solution:
    def maxTwoEvents(self, arr: List[List[int]]) -> int:
        arr.sort()
        k = arr[-1][-1]
        temp = []

        for i in range(len(arr)-1, -1, -1):
            k = max(k, arr[i][-1])

            temp.append(k)

        temp = temp[::-1]
        
        jvrc = 0

        def fa(f, r, k):
            ans = False
            
            while f <= r:
                mid = (f + r)//2

                if arr[mid][0] > k:
                    r = mid-1
                    ans = mid
                else:
                    f = mid+1
            
            return ans
        
        for i in range(len(arr)):
            m = fa(i+1, len(arr)-1, arr[i][1])
            c = arr[i][-1]

            if m != False:
                c += temp[m]
            
            jvrc = max(jvrc, c)

        return jvrc

        