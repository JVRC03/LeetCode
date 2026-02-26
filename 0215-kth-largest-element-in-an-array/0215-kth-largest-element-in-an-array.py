class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k-=1
        heap = []
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
        
        while k:
            k -= 1
            heapq.heappop(heap)

        return -heap[0]
        