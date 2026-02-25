class Solution:
    def sortByBits(self, jvrc: List[int]) -> List[int]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(jvrc)):
            k = bin(jvrc[i])
            k = k[2:]
            c = k.count('1')

            heapq.heappush(heap, [c, jvrc[i]])

        jvrc = []
        while len(heap):
            a = heapq.heappop(heap)
            jvrc.append(a[-1])
        
        return jvrc
        