class Solution:

    def __init__(self):
        self.jvrc = float('inf')

    def minScore(self, n: int, arr: List[List[int]]) -> int:

        dic = {}

        for i in range(len(arr)):
            if arr[i][0] not in dic:
                dic[arr[i][0]] = [[arr[i][1], arr[i][-1]]]
            else:
                dic[arr[i][0]].append([arr[i][1], arr[i][-1]])
            
            if arr[i][1] not in dic:
                dic[arr[i][1]] = [[arr[i][0], arr[i][-1]]]
            else:
                dic[arr[i][1]].append([arr[i][0], arr[i][-1]])
        
        v = [0] * (n+1)

        def f(s):
            if v[s]:
                return 
            v[s] = 1
            a = dic[s]

            for i in range(len(a)):
                self.jvrc = min(self.jvrc, a[i][-1])
                f(a[i][0])

        f(1)
        return self.jvrc


        