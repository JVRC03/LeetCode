class Solution:
    def watchedVideosByFriends(self, w: List[List[str]], e: List[List[int]], source: int, b: int):
        dic = {}

        q = deque([source])
        v = [0] * len(e)
        

        while b:
            b -= 1
            c = len(q)

            for i in range(c):
                s = q.popleft()
                v[s] = 1

                temp = e[s]
                
                for j in range(len(temp)):
                    if not v[temp[j]]:
                        q.append(temp[j])
                        v[temp[j]] = 1
            
        wa = []
        for i in q:
            wa.append(i)
        
        q = wa.copy()
        for i in range(len(q)):
            for j in range(len(w[q[i]])):
                if w[q[i]][j] not in dic:
                    dic[w[q[i]][j]] = 1
                else:
                    dic[w[q[i]][j]] += 1
        
        x = []
        for i in dic:
            x.append([dic[i], i])
        
        x.sort()
        jvrc = []

        for i in range(len(x)):
            jvrc.append(x[i][-1])
        
        return jvrc

        