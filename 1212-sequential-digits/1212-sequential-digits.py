class Solution:
    def sequentialDigits(self, l: int, r: int) -> List[int]:
        jvrc, heap = [], []
        heapq.heapify(heap)

        glob = 1
    
        while glob < 10:
            s = ''
            c = glob
            while c < 10:
                s += str(c)
                c += 1

                if l <= int(s) <= r:
                    heapq.heappush(heap, int(s))
                if int(s) > r:
                    break
            
            glob += 1

        while len(heap):
            jvrc.append(heapq.heappop(heap))
        
        return jvrc

            

        
