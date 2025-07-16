class Solution:
    def restoreArray(self, arr: List[List[int]]) -> List[int]:
        dic = {}

        for i in range(len(arr)):
            if arr[i][0] not in dic:
                dic[arr[i][0]] = [arr[i][1]]
            else:
                dic[arr[i][0]].append(arr[i][1])
            
            if arr[i][1] not in dic:
                dic[arr[i][1]] = [arr[i][0]]
            else:
                dic[arr[i][1]].append(arr[i][0])
        
        curr = -1

        for i in dic:
            if len(dic[i]) == 1:
                curr = i
                break
        
        jvrc = [curr, dic[curr][0]]
        
        while len(jvrc) < len(dic):
            curr = jvrc[-1]
            n = dic[curr]
            i = -2
            while len(n):
                a = n.pop()
                if a == jvrc[i]:
                    continue
                i -= 1
                jvrc.append(a)
        
        return jvrc


        