class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        mid = arr[(len(arr)-1)//2]
        heap = []
        
        heapq.heapify(heap)

        for i in range(len(arr)):
            heapq.heappush(heap, [-(abs(arr[i]-mid)), -arr[i]])
        
        jvrc = []

        while k:
            k -= 1
            temp = heapq.heappop(heap)
            jvrc.append(-(temp[1]))
        
        return jvrc
        