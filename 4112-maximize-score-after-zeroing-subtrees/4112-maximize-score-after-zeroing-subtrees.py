class Solution:
    def maxScore(self, par: list[int], op: list[int], k: list[int]) -> int:
        dic = {}

        for i in range(len(par)):
            if par[i] not in dic:
                dic[par[i]] = [i]
            else:
                dic[par[i]].append(i)
        
        def func(source):
            if source not in dic:
                if source == -1:
                    return 0
                return k[source]
            
            arr = dic[source]
            val = []

            for i in range(len(arr)):
                val.append(func(arr[i]))
            
            if op[source] == 0:
                mini = min(val)
                ans, c = 0, 0

                for i in range(len(val)):
                    if val[i] != mini:
                        ans += val[i]
                    else:
                        if c == 0:
                            c = 1
                        else:
                            ans += val[i]
                if mini >= 0:
                    return k[source] + sum(val)
                return k[source] + ans
            
            return k[source] + (sum(val) - min(val))

        return func(0)
        