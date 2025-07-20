class Solution:
    def maxDistance(self, nums: List[List[int]]) -> int:
        min_heap, max_heap = [], []
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        for i in range(len(nums)):
            heapq.heappush(min_heap, [nums[i][0], i])
            heapq.heappush(min_heap, [nums[i][-1], i])

            heapq.heappush(max_heap, [-nums[i][0], i])
            heapq.heappush(max_heap, [-nums[i][-1], i])
        
        jvrc = 0

        for i in range(len(nums)):
            a, b, c ,d = -1, -1, -1, -1

            if i != min_heap[0][-1]:
                a = abs(nums[i][0] - min_heap[0][0])
            else:
                f = heapq.heappop(min_heap)
                a = abs(nums[i][0] - min_heap[0][0])
                heapq.heappush(min_heap, f)

            if i != max_heap[0][-1]:
                b = abs(nums[i][0] - (-max_heap[0][0]))
            else:
                f = heapq.heappop(max_heap)
                b = abs(nums[i][0] - (-max_heap[0][0]))
                heapq.heappush(max_heap, f)

            if i != min_heap[0][-1]:
                c = abs(nums[i][-1] - min_heap[0][0])
            else:
                f = heapq.heappop(min_heap)
                c = abs(nums[i][-1] - min_heap[0][0])
                heapq.heappush(min_heap, f)


            if i != max_heap[0][-1]:
                d = abs(nums[i][-1] - (-max_heap[0][0]))
            else:
                f = heapq.heappop(max_heap)
                d = abs(nums[i][-1] - (-max_heap[0][0]))
                heapq.heappush(max_heap, f)

            jvrc = max(jvrc, a, b, c, d)
        
        return jvrc
        