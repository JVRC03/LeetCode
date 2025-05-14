class Solution:
    def filterRestaurants(self, res: List[List[int]], k: int, mp: int, md: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        jvrc = []

        for i in range(len(res)):
            if k == 1:
                if res[i][2] == k and res[i][3] <= mp and res[i][4] <= md:
                    temp = [-res[i][1], -res[i][0]]
                    heapq.heappush(heap, temp)
            else:
                if res[i][3] <= mp and res[i][4] <= md:
                    temp = [-res[i][1], -res[i][0]]
                    heapq.heappush(heap, temp)
        
        while len(heap):
            a = heapq.heappop(heap)
            jvrc.append(abs(a[1]))

        return jvrc

        