class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(y)):
            heapq.heappush(heap, [-y[i], i])
        
        jvrc = -1

        while len(heap) >= 3:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            c = heapq.heappop(heap)

            if (x[a[1]] != x[b[1]]) and (x[b[1]] != x[c[1]]) and(x[a[1]] != x[c[1]]):
                jvrc = abs(a[0]+b[0]+c[0])
                break
            
            if x[a[1]] == x[b[1]]:
                heapq.heappush(heap, a)
                heapq.heappush(heap, c)
            else:
                heapq.heappush(heap, a)
                heapq.heappush(heap, b)

        return jvrc