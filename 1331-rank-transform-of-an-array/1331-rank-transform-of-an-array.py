class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = []
        dic = {}

        heapq.heapify(heap)

        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = -1
                heapq.heappush(heap, arr[i])
        
        c = 1
        while len(heap):
            dic[heapq.heappop(heap)] = c
            c += 1
        
        jvrc = []

        for i in range(len(arr)):
            jvrc.append(dic[arr[i]])
        
        return jvrc
        



        

        