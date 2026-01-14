class Solution:
    def equationsPossible(self, arr: List[str]):
        dic = {}
        s = set()

        for i in range(len(arr)):
            if arr[i][1] == '=':
                if arr[i][0] not in dic:
                    dic[arr[i][0]] = [arr[i][-1]]
                else:
                    dic[arr[i][0]].append(arr[i][-1])
            
                if arr[i][-1] not in dic:
                    dic[arr[i][-1]] = [arr[i][0]]
                else:
                    dic[arr[i][-1]].append(arr[i][0])
        
        def dfs(source):
            if source in s:
                return set()
            
            s.add(source)
            if source not in dic:
                return {source}
            
            temp = dic[source]
            glob = {source}

            for i in range(len(temp)):
                k = dfs(temp[i])
                glob |= k
            
            return glob

        temp = {}

        for i in dic:
            if i not in s:
                temp[i] = dfs(i)
        
        check = {}
        c = 0

        for i in temp:
            x = list(temp[i])
            check[i] = c

            for j in range(len(x)):
                check[x[j]] = c
            
            c += 1

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][-1]

            if a not in check or b not in check:
                if a == b and arr[i][1]=='!':
                    return False
                continue

            if check[a] == check[b] and arr[i][1] == '=':
                continue

            if check[a] != check[b] and arr[i][1] == '!':
                continue

            return False 

        return True


        