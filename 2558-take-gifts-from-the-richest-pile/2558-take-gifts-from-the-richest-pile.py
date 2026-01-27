class Solution:
    def pickGifts(self, arr: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(arr)):
            heapq.heappush(heap, -arr[i])
        
        while k and len(heap):
            temp = int(math.sqrt(abs(heapq.heappop(heap))))
            k -= 1

            heapq.heappush(heap, -temp)
        
        return abs(sum(heap))


        