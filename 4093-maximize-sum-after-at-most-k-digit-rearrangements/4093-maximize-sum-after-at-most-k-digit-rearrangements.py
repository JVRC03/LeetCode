class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        def rev(n):
            s = str(n)
            l = list(s)
            l.sort()

            l = l[::-1]
            return int(''.join(l))

        s = set()
        jvrc = 0
        for i in range(len(nums)):
            revv = rev(nums[i])

            if revv > nums[i]:
                heapq.heappush(heap, [-(revv - nums[i]), -revv, i])

        while k and len(heap):
            k -= 1
            arr = heapq.heappop(heap)

            jvrc += abs(arr[1])
            s.add(arr[-1])
        
        for i in range(len(nums)):
            if i not in s:
                jvrc += nums[i]

        return jvrc
