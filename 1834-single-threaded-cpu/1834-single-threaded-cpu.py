class Solution:
    def getOrder(self, nums: List[List[int]]) -> List[int]:
        arr, heap = [], []
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, [nums[i][0], nums[i][1], i])
        
        while len(heap):
            arr.append(heapq.heappop(heap))
        
        heapq.heapify(heap)
        jvrc = [arr[0][-1]]
        curr = arr[0][0]+arr[0][1]

        for i in range(1, len(arr)):
            if curr >= arr[i][0]:
                heapq.heappush(heap, [arr[i][1], arr[i][-1]])
                continue
            
            while len(heap) and curr < arr[i][0]:
                temp = heapq.heappop(heap)
                curr += temp[0]
                jvrc.append(temp[-1])
            
            if arr[i][0] > curr:
                curr = arr[i][0]
            
            heapq.heappush(heap, [arr[i][1], arr[i][-1]])
        
        while len(heap):
            temp = heapq.heappop(heap)
            jvrc.append(temp[-1])
        
        return jvrc




        