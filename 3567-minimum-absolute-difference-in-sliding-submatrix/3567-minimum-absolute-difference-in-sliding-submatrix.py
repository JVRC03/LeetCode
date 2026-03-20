class Solution:
    def minAbsDiff(self, mat: List[List[int]], k: int) -> List[List[int]]:
        jvrc = []

        def bring(arr):
            arr.sort()

            mini = float('inf')

            for i in range(len(arr)-1):
                if arr[i] == arr[i+1]:
                    continue
                diff = abs(arr[i+1]-arr[i])
                mini = min(mini, diff)

            if mini == float('inf'):
                return 0
            
            return mini

        for i in range(len(mat)-k+1):
            ans = []
            for j in range(len(mat[0])-k+1):
                temp = []
                for l in range(k):
                    for m in range(k):
                        temp.append(mat[i+l][j+m])
                
                ans.append(bring(temp))
            
            jvrc.append(ans)
        
        return jvrc


