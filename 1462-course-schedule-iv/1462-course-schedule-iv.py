class Solution:
    def checkIfPrerequisite(self, n: int, arr: List[List[int]], jvrc: List[List[int]]):
        dic, temp = {}, {}

        for i in range(n):
            temp[i] = [i]
        
        for i in range(len(arr)):
            temp[arr[i][-1]].append(arr[i][0])

        def dfs(source, curr):
            if v[source]:
                return dic[source]
            
            v[source] = 1

            a = temp[source]
            glob = {source}

            for i in range(len(a)):
                if a[i] != source:
                    curr.add(a[i])
                    k = dfs(a[i], curr)
                    curr.remove(a[i])
                    glob |= k
            
            dic[source] = glob

            return dic[source]

        v = [0] * n

        for i in range(n):
            if not v[i]:
                dfs(i, set())

        for i in range(len(jvrc)):
            if jvrc[i][0] in dic[jvrc[i][1]]:
                jvrc[i] = True
            else:
                jvrc[i] = False

        return jvrc
        