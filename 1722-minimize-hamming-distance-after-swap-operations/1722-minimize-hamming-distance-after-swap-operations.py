class Solution:

    def __init__(self):
        self.temp = []
        self.t = {}

    def minimumHammingDistance(self, a: List[int], b: List[int], k: List[List[int]]):
        dic = {}

        for i in range(len(k)):
            if k[i][0] not in dic:
                dic[k[i][0]] = [k[i][-1]]
            else:
                dic[k[i][0]].append(k[i][-1])
            
            if k[i][-1] not in dic:
                dic[k[i][-1]] = [k[i][0]]
            else:
                dic[k[i][-1]].append(k[i][0])
            
        v = [0] * len(a)
        jvrc = 0

        def dfs(source):
            if source not in dic or v[source]:
                return 
            arr = dic[source]
            v[source] = 1

            self.temp.append(a[source])
            if b[source] not in self.t:
                self.t[b[source]] = 1
            else:
                self.t[b[source]] += 1

            for i in range(len(arr)):
                dfs(arr[i])

        for i in range(len(v)):
            if not v[i]:
                self.temp = []
                self.t = {}
                dfs(i)

                while len(self.temp):
                    s = self.temp.pop()

                    if s in self.t:
                        self.t[s] -= 1
                        if not self.t[s]:
                            del self.t[s]
                        continue
                    
                    jvrc += 1
        
        for i in range(len(v)):
            if not v[i]:
                if a[i] != b[i]:
                    jvrc += 1
        
        return jvrc


            



            



        