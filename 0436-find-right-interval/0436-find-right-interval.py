class Solution:
    def findRightInterval(self, arr: List[List[int]]) -> List[int]:
        temp = arr.copy()
        temp.sort()

        def f(k, i):
            f, r = 0, len(arr)-1
            ans = float('inf')

            while f <= r:
                mid = (f+r)//2

                if temp[mid][0] >= k:
                    r = mid-1
                    ans = temp[mid][0]
                else:
                    f = mid+1
            
            return ans

        jvrc = []
        dic = {}

        for i in range(len(arr)):
            dic[arr[i][0]] = i

        for i in range(len(arr)):
            l = f(arr[i][1], i)
            if l == float('inf'):
                jvrc.append(-1)
                continue
            jvrc.append(dic[l])
        
        return jvrc


        