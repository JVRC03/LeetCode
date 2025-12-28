class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        arr = list(s)
        f, r = 0, len(nums)
        jvrc = 0

        while len(arr) and arr[-1] == '0':
            arr.pop()
            r -= 1
        
        arr = arr[::-1]
        
        while len(arr) and arr[-1] == '1':
            jvrc += nums[f]
            f += 1
            arr.pop()
        
        arr = arr[::-1]
            
        heap = []
        heapq.heapify(heap)
        c = 0

        for i in range(f, r):
            heapq.heappush(heap, -nums[i])
            if arr[c] == '0':
                c += 1
                continue
            jvrc += abs(heapq.heappop(heap))
            c += 1
            
        return jvrc
        
        


        