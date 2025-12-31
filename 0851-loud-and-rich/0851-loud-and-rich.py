class Solution:
    def loudAndRich(self, arr: List[List[int]], k: List[int]) -> List[int]:
        jvrc = [-1] * len(k)
        dic = {}

        for i in range(len(k)):
            dic[i] = [i]

        for i in range(len(arr)):
            dic[arr[i][-1]].append(arr[i][0])
        
        def dfs(source):
            if len(dic[source]) == 1:
                jvrc[source] = source
                return k[source], source
            
            if jvrc[source] != -1:
                return k[jvrc[source]], jvrc[source]
            
            temp = dic[source]
            curr, global_maxi = float('inf'), 0

            for i in range(1, len(temp)):
                a, b = dfs(temp[i])
                
                if curr > a:
                    curr = a
                    global_maxi = b

            jvrc[source] = global_maxi

            if curr > k[temp[0]]:
                jvrc[source] = source
                curr = k[temp[0]]
                global_maxi = source 

            return curr, global_maxi
                
        for i in range(len(k)):
            if jvrc[i] == -1:
                dfs(i)
        
        return jvrc

        
        