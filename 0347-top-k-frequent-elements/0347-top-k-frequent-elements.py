class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        for i in dic:
            heapq.heappush(heap, [-dic[i], i])
        
        jvrc = []

        while k:
            k -= 1
            arr = heapq.heappop(heap)

            jvrc.append(arr[-1])
        
        return jvrc



        