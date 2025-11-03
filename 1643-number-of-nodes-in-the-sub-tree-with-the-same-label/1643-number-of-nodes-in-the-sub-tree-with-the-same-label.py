class Solution:
    def __init__(self):
        self.ans = {}

    def countSubTrees(self, n: int, arr: List[List[int]], s: str) -> List[int]:
        if n == 1:
            return [1]
        jvrc, v = [], [0] * n
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
            if v[source]:
                return {}
            
            v[source] = 1
            arr = dic[source]
            loc = {}

            for i in range(len(arr)):
                recur_dic = dfs(arr[i])
                for j in recur_dic:
                    if j not in loc:
                        loc[j] = recur_dic[j]
                    else:
                        loc[j] += recur_dic[j]
            
            if s[source] not in loc:
                loc[s[source]] = 1
            else:
                loc[s[source]] += 1
            
            self.ans[source] = loc[s[source]]
            return loc

        dfs(0)
        
        for i in range(n):
            jvrc.append(self.ans[i])
        
        return jvrc
        





        