class Solution:
    def clearStars(self, s: str) -> str:
        dic = {}
        jvrc = ''
        arr = []
        heapq.heapify(arr)

        for i in range(len(s)):
            if s[i] != '*':
                cont = 1
                for j in range(len(arr)):
                    if arr[j][0] == s[i]:
                        arr[j][1] += 1
                        cont = 0
                        break

                if s[i] not in dic:
                    dic[s[i]] = [i]
                else:
                    dic[s[i]].append(i)

                if cont:
                    heapq.heappush(arr, [s[i], 1])
            else:
                if len(arr):
                    k = heapq.heappop(arr)
                    if k[1]-1:
                        temp = [k[0], k[1]-1]
                        heapq.heappush(arr, temp)
                    if k[0] in dic:
                        dic[k[0]].pop()
                        if len(dic[k[0]]) == 0:
                            del dic[k[0]]

        for i in dic:
            dic[i] = set(dic[i])

        for i in range(len(s)):
            
            if (s[i] in dic) and (i in dic[s[i]]):
                jvrc += s[i]
                continue
        
        return jvrc
                
        