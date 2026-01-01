class Solution:
    def getAncestors(self, n: int, arr: List[List[int]]) -> List[List[int]]:
        temp, dic = {}, {}
        jvrc = []

        for i in range(n):
            temp[i] = []
            dic[i] = {i}

        for i in range(len(arr)):
            temp[arr[i][-1]].append(arr[i][0])
        
        def dfs(source, curr):
            if len(temp[source]) == 0:
                if not v[source]:
                    v[source] = 1
                return {source}
            
            if v[source]:
                return dic[source]
            
            v[source] = 1
            a = temp[source]
            glob = set()

            for i in range(len(a)):
                curr.add(a[i])
                k = dfs(a[i], curr)
                glob |= k
                curr.remove(a[i])
            
            dic[source] |= glob

            if not len(dic[source]):
                return {source}

            return dic[source]

        v = [0] * n
        for i in range(n):
            if not v[i]:
                dfs(i, set())
        
        for i in dic:
            dic[i].remove(i)
            k = list(dic[i])
            k.sort()
            jvrc.append(k)
    
        return jvrc


        

        