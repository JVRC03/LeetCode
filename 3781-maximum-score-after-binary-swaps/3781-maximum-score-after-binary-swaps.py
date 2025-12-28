class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        jvrc = 0
        heap = []
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
            if s[i] == '0':
                continue
            jvrc += abs(heapq.heappop(heap))
            
        return jvrc
        
        


        