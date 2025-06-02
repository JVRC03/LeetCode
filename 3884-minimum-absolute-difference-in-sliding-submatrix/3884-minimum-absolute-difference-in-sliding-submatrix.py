class Solution:
    def minAbsDiff(self, mat: List[List[int]], k: int) -> List[List[int]]:
        jvrc = []

        def f(arr):
            r = set(arr)
            arr = list(r)
            ans = float('inf')
            arr.sort()
            if len(arr) == 1:
                return 0
            
            for i in range(1, len(arr)):
                ans = min(ans, abs(arr[i-1]-arr[i]))
            
            return ans


        for i in range(len(mat)-k+1):
            temp = []

            for j in range(len(mat[0])-k+1):
                arr = []
                for l in range(k):
                    for m in range(k):
                        arr.append(mat[i+l][j+m])

                temp.append(f(arr))

            jvrc.append(temp)
        
        return jvrc
                

        