class Solution:
    def __init__(self):
        self.jvrc = 0

    def countGoodNodes(self, arr: List[List[int]]) -> int:
        maxi = 0
        dic = {}

        for i in range(len(arr)):
            if arr[i][0] not in dic:
                dic[arr[i][0]] = [arr[i][-1]]
            else:
                dic[arr[i][0]].append(arr[i][-1])

            if arr[i][-1] not in dic:
                dic[arr[i][-1]] = [arr[i][0]]
            else:
                dic[arr[i][-1]].append(arr[i][0])
        
            maxi = max(maxi, max(arr[i]))
        
        v = [0] * (maxi + 1)

        def dfs(source):
            if v[source]:
                return float('-inf')
            v[source] = 1

            temp = dic[source]
            c, tim = 0, []

            for i in range(len(temp)):
                k = dfs(temp[i])
                tim.append(k)
                if k >= 0:
                    c += k
                
            tim.sort()
            if source != 0:
                tim.pop(0)

            if not len(tim):
                self.jvrc += 1
                return 1

            if tim[-1] == tim[0]:
                self.jvrc += 1
            
            return c+1

        dfs(0)
        return self.jvrc

        