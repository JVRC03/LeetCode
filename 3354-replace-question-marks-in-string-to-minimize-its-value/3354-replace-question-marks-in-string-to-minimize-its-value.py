class Solution:
    def minimizeStringValue(self, s: str) -> str:
        dic, f = {}, 0

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        heap, arr = [], []
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

        for i in range(len(s)):
            if s[i] != '?':
                continue
            
            a = heapq.heappop(heap)
            arr.append(a[-1])
            a[0] += 1

            heapq.heappush(heap, a)
        
        arr.sort()
        for i in range(len(s)):
            if s[i] != '?':
                jvrc += s[i]
            else:
                jvrc += arr[f]
                f += 1

        return jvrc

        