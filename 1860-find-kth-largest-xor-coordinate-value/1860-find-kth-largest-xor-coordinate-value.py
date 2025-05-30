class Solution:
    def kthLargestValue(self, mat: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] ^= mat[i][j-1]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp = mat[i][j]
                
                if i-1 >= 0:
                    temp ^= mat[i-1][j]
                    
                mat[i][j] = temp
                heapq.heappush(heap, -temp)
        
        jvrc = 0
        while k:
            k -= 1
            jvrc = abs(heapq.heappop(heap))
        
        return jvrc
        
                




        