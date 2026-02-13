class Solution:

    def sortByReflection(self, nums: List[int]) -> List[int]:
        jvrc = []
        heap = []

        heapq.heapify(heap)

        for i in range(len(nums)):
            s = bin(nums[i])
            s = s[2:]
            s = s[::-1]
            k = int(s, 2)

            heapq.heappush(heap, [k, nums[i]])
        
        while len(heap):
            a = heapq.heappop(heap)
            jvrc.append(a[-1])
        
        return jvrc
        
        