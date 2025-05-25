class Solution:
    def maximumBags(self, cap: List[int], rock: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        jvrc = 0

        for i in range(len(cap)):
            if cap[i]-rock[i] == 0:
                jvrc += 1
                continue
            heapq.heappush(heap, [cap[i]-rock[i], i])
        
        while k:
            if len(heap):
                a = heapq.heappop(heap)
                if k >= a[0]:
                    jvrc += 1
                    k -= a[0]
                continue
            break
            
        
        return jvrc
        