class Solution:
    def heightChecker(self, arr: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(arr)):
            heapq.heappush(heap, arr[i])
        
        jvrc, i = 0, 0
        while len(heap):
            if arr[i] != heapq.heappop(heap):
                jvrc += 1
            
            i += 1
        
        return jvrc
        