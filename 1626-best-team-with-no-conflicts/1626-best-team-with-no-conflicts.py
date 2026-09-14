class Solution:
    def bestTeamScore(self, arr: List[int], a: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(a)):
            heapq.heappush(heap, [a[i], arr[i]])
        
        arr = []
        while len(heap):
            a = heapq.heappop(heap)
            arr.append(a[-1])

        dp = []
        for i in range(len(arr)):
            dp.append([-1] * len(arr))
        
        def func(i, prev):
            if i == len(arr):
                return 0
            
            if prev != -1 and dp[i][prev] != -1:
                return dp[i][prev]

            take = 0
            if prev == -1 or arr[prev] <= arr[i]:
                take = arr[i] + func(i + 1, i)
            not_take = func(i + 1, prev)

            dp[i][prev] = max(take, not_take)
            return dp[i][prev]

        return func(0, -1)
        