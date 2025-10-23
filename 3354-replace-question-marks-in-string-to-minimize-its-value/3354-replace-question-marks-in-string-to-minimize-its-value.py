class Solution:
    def minimizeStringValue(self, s: str) -> str:
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        heap = []
        heapq.heapify(heap)

        for i in range(26):
            k = chr(97+i)
            temp = []

            if k not in dic:
                temp = [0, k]
            else:
                temp = [dic[k], k]
            heapq.heappush(heap, temp)
        
        jvrc = ''
        arr = []

        for i in range(len(s)):
            if s[i] != '?':
                continue
            
            a = heapq.heappop(heap)
            arr.append(a[-1])
            a[0] += 1

            heapq.heappush(heap, a)
        
        arr.sort()
        arr = arr[::-1]

        for i in range(len(s)):
            if s[i] != '?':
                jvrc += s[i]
            else:
                jvrc += arr[-1]
                arr.pop()

        return jvrc

        