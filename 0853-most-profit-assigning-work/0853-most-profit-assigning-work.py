class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], arr: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        def f(a, k):
            f, r = 0, len(a)-1
            c = -1

            while f <= r:
                mid = (f+r)//2

                if a[mid][0] > k:
                    r = mid-1
                else:
                    c = mid
                    f = mid+1
            
            return c
            
        for i in range(len(d)):
            temp = [d[i], -p[i]]
            heapq.heappush(heap, temp)

        nums = []
        n = []
        curr = -1

        while len(heap):
            nums.append(heapq.heappop(heap))
            curr = max(curr, abs(nums[-1][-1]))
            n.append(curr)
        
        jvrc = 0

        for i in range(len(arr)):
            k = f(nums, arr[i])
            
            if k!=-1:
                jvrc += n[k]
        
        return jvrc
        