class Solution:
    def getFinalState(self, nums: List[int], k: int, n: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, [nums[i], i])
        
        while k:
            k -= 1

            a = heapq.heappop(heap)
            nums[a[-1]] *= n
            heapq.heappush(heap, [nums[a[-1]], a[-1]])
        
        return nums

        