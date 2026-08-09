class Solution:
    def weightedSum(self, p: list[int], arr: list[int]) -> int:
        dic = {}

        for i in range(len(p)):
            if p[i] not in dic:
                dic[p[i]] = [i]
            else:
                dic[p[i]].append(i)
        
        self.jvrc = 0
        def height(root):
            if root not in dic:
                return 0

            a = dic[root]

            glob = 1
            for i in range(len(a)):
                glob = max(glob, 1 + height(a[i]))
            return glob

        h = height(0)
        h += 1

        def dfs(root, curr, arr):
            self.jvrc += (arr[root] * (h - curr + 1))

            if root not in dic:
                return 0
            
            a = dic[root]

            for i in range(len(a)):
                dfs(a[i], curr + 1, arr)

        dfs(0, 1, arr)
        return self.jvrc








        