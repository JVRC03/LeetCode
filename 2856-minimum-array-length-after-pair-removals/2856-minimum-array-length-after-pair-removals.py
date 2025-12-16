class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        jvrc, dic = 0, {}
        heap = []

        heapq.heapify(heap)

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        for i in dic:
            k = [-dic[i], i]
            heapq.heappush(heap, k)
    
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)

            a[0] += 1
            b[0] += 1

            if a[0]:
                heapq.heappush(heap, a)
            if b[0]:
                heapq.heappush(heap, b)
            
        while len(heap):
            c = heapq.heappop(heap)

            jvrc += abs(c[0])    
        
        return jvrc
            

            


        