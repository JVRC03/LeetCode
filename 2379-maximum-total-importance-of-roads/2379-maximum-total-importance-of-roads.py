class Solution:
    def maximumImportance(self, n: int, g: List[List[int]]) -> int:
        dic = {}

        for i in range(len(g)):
            if g[i][0] not in dic:
                dic[g[i][0]] = 1
            else:
                dic[g[i][0]] += 1

            if g[i][-1] not in dic:
                dic[g[i][-1]] = 1
            else:
                dic[g[i][-1]] += 1
        
        arr = list(dic.values())
        arr.sort()
        jvrc = 0

        while len(arr):
            jvrc += (n * arr[-1])
            n -= 1
            arr.pop()
        
        return jvrc

        