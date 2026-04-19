class Solution:
    def colorGrid(self, n: int, m: int, arr: list[list[int]]) -> list[list[int]]:
        mat = []
        for i in range(n):
            temp = [0] * m
            mat.append(temp)
        
        q = deque([])
        for i in range(len(arr)):
            q.append(arr[i])
            mat[arr[i][0]][arr[i][1]] = arr[i][2]
        
        while len(q):
            c = len(q)
            dic = {}

            for i in range(c):
                pair = q.popleft()
                r, c = pair[0], pair[1]
                val = pair[2]

                if r-1 >= 0 and mat[r-1][c] == 0:
                    k = str(r-1) + '-' + str(c)
                    if k not in dic:
                        dic[k] = val
                    else:
                        dic[k] = max(dic[k], val)
                
                if r+1 < n and mat[r+1][c] == 0:
                    k = str(r+1) + '-' + str(c)
                    if k not in dic:
                        dic[k] = val
                    else:
                        dic[k] = max(dic[k], val)

                if c-1 >= 0 and mat[r][c-1] == 0:
                    k = str(r) + '-' + str(c-1)
                    if k not in dic:
                        dic[k] = val
                    else:
                        dic[k] = max(dic[k], val)
                
                if c+1 < m and mat[r][c+1] == 0:
                    k = str(r) + '-' + str(c+1)
                    if k not in dic:
                        dic[k] = val
                    else:
                        dic[k] = max(dic[k], val)
            
            for i in dic:
                a = i.split('-')
                r, c = int(a[0]), int(a[1])

                mat[r][c] = dic[i]
                q.append([r, c, dic[i]])
        
        return mat





        