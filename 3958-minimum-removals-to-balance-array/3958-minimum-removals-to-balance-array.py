class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        c = 0
        jvrc = float('inf')
        nums.sort()

        def f(n):
            f, r = 0, len(nums)-1
            a = -1

            while f <= r:
                mid = (f+r)//2

                if nums[mid] <= n:
                    f = mid+1
                else:
                    a = mid
                    r = mid-1
            
            return a

        for i in range(len(nums)):
            g = f(k * nums[i])
            if g == -1:
                jvrc = min(jvrc, c)
                continue
            jvrc = min(jvrc, c+(len(nums)-g))
            c += 1

        return jvrc
        