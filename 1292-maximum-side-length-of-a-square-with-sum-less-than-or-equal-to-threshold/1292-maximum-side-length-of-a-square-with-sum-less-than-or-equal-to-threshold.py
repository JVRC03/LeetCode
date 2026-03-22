class Solution:
    def maxSideLength(self, mat: List[List[int]], k: int) -> int:
        f, r = 1, max(len(mat), len(mat[0]))
        jvrc = 0
        p_sum = []

        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                if not len(temp):
                    temp.append(mat[i][j])
                else:
                    temp.append(temp[-1] + mat[i][j])
            p_sum.append(temp)
            
        def check(idx, mat, k):
            for i in range(len(mat) - idx + 1):
                for j in range(len(mat[0]) - idx + 1):
                    curr = 0
                    for l in range(idx):
                        if j == 0:
                            curr += p_sum[l+i][j+idx-1]
                        else:
                            curr += (p_sum[l+i][j+idx-1] - p_sum[l+i][j-1])
                   
                    if curr <= k:
                        return True
            
            return False

        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, mat, k):
                jvrc = max(jvrc, mid)
                f = mid+1
            else:
                r = mid-1
        
        return jvrc
        