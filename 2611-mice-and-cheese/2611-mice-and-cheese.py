class Solution:
    def miceAndCheese(self, a: List[int], b: List[int], k: int) -> int:
        s = set()
        heap = []
        heapq.heapify(heap)

        for i in range(len(a)):
            heapq.heappush(heap, [-(a[i]-b[i]), i])
        
        jvrc = 0

        while k:
            k -= 1
            n = heapq.heappop(heap)
            s.add(n[-1])
            jvrc += (a[n[-1]])
        
        for i in range(len(a)):
            if i not in s:
                jvrc += b[i]
        
        return jvrc
        


        