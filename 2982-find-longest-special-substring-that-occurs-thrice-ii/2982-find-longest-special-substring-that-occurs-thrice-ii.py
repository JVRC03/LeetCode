class Solution:
    def maximumLength(self, s: str) -> int:
        jvrc = float('-inf')
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)
        
        def get(arr):
            temp = []
            c = 0

            for i in range(len(arr)):
                if i == 0:
                    c = 1
                    continue
                if arr[i] == arr[i-1] + 1:
                    c += 1
                else:
                    temp.append(c)
                    c = 1
            
            temp.append(c)
            return temp

        for i in dic:
            dic[i] = get(dic[i])
        
        for i in dic:
            if len(dic[i]) >= 2:
                arr = dic[i]
                arr.sort()
                for j in range(len(arr)):
                    c = 0
                    for k in range(j+1, len(arr)):
                        if arr[k] >= arr[j]:
                            c += 1
                        if c >= 2:
                            break
                    if c >= 2:
                        jvrc = max(jvrc, arr[j])
                
                if arr[-1] > arr[-2]:
                    jvrc = max(jvrc, arr[-2])
                else:
                    jvrc = max(jvrc, arr[-2]-1)
                
                jvrc = max(jvrc, arr[-1]-2)

            else:
                a = dic[i][0]
                if a >= 3:
                    jvrc = max(jvrc, a-2)

        if jvrc <= 0:
            jvrc = -1

        return jvrc

        