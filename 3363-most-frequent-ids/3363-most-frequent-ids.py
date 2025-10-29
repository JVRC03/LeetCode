class Solution:
    def mostFrequentIDs(self, jvrc: List[int], freq: List[int]) -> List[int]:
        dic = {}
        heap = []
        heapq.heapify(heap)

        for i in range(len(jvrc)):
            if jvrc[i] not in dic:
                dic[jvrc[i]] = [freq[i], i]
                heapq.heappush(heap, [-freq[i], jvrc[i], i])
            else:
                dic[jvrc[i]][0] += freq[i]
                dic[jvrc[i]][1] = i
                temp = [-dic[jvrc[i]][0], jvrc[i], i]

                while len(heap):
                    if dic[heap[0][1]][-1] != heap[0][-1]:
                        heapq.heappop(heap)
                        continue
                    break
                
                heapq.heappush(heap, temp)
            
            jvrc[i] = abs(heap[0][0])
        
        return jvrc
                
        