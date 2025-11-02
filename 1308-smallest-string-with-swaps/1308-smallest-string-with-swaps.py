class Solution:
    def __init__(self):
        self.val = []
        self.idx = []

    def smallestStringWithSwaps(self, s: str, arr: List[List[int]]) -> str:
        v = [0] * len(s)
        jvrc = list(s)
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
            
        def dfs(source):
            if v[source] == 1:
                return
            if source not in dic:
                return 
            v[source] = 1
            temp = dic[source]

            heapq.heappush(self.idx, source)
            heapq.heappush(self.val, s[source])

            for i in range(len(temp)):
                dfs(temp[i])

        for i in range(len(s)):
            if v[i] == 0:
                self.idx, self.val = [], []
                heapq.heapify(self.idx)
                heapq.heapify(self.val)
                
                dfs(i)
                while len(self.idx):
                    k = heapq.heappop(self.idx)
                    jvrc[k] = heapq.heappop(self.val)
                
        return ''.join(jvrc)





        