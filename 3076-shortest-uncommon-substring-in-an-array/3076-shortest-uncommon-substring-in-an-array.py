class Solution:
    def shortestSubstrings(self, arr):
        dic = {}
        jvrc = []

        def call(temp):
            curr = ''

            for i in temp:
                if i in dic and dic[i] == temp[i]:
                    if len(curr) == 0:
                        curr = i
                    else:
                        if len(i) < len(curr):
                            curr = i
                        elif len(i) == len(curr):
                            curr = min(curr, i)
            
            return curr

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                curr = ''
                for k in range(j, len(arr[i])):
                    curr += arr[i][k]
                    if curr not in dic:
                        dic[curr] = 1
                    else:
                        dic[curr] += 1
        
        for i in range(len(arr)):
            temp = {}
            for j in range(len(arr[i])):
                curr = ''
                for k in range(j, len(arr[i])):
                    curr += arr[i][k]
                    if curr not in temp:
                        temp[curr] = 1
                    else:
                        temp[curr] += 1
            
            res = call(temp)
            jvrc.append(res)
        
        return jvrc



        