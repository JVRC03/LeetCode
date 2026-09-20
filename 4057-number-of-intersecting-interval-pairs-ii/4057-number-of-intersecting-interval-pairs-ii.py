class Solution:
    def countIntersectingIntervals(self, arr: list[list[int]]) -> int:
        arr.sort()
        jvrc = 0

        def func(k, ff, arr):
            f, r = ff, len(arr) - 1
            ans = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid][0] <= k:
                    f = mid + 1
                    ans = mid
                else:
                    r = mid - 1

            return ans

        for i in range(len(arr)):
            idx = func(arr[i][1], i + 1, arr)
            if idx > 0:
                jvrc += (idx - i)

        return jvrc
        