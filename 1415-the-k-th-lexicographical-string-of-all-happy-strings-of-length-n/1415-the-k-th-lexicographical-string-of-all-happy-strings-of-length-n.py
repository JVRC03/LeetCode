class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.jvrc = []
        self.vis = set()

        def dfs(n, curr, arr):
            if len(curr) > n:
                return
            
            if len(curr) == n:
                self.vis.add(curr)
                return
            
            for i in range(len(arr)):
                if not len(curr):
                    dfs(n, curr + arr[i], arr)
                else:
                    if curr[-1] != arr[i]:
                        dfs(n, curr + arr[i], arr)
                    else:
                        continue

        dfs(n, '', ['a', 'b', 'c'])
        self.jvrc = list(self.vis)
        self.jvrc.sort()
        if k > len(self.jvrc):
            return ''
        return self.jvrc[k-1]
        