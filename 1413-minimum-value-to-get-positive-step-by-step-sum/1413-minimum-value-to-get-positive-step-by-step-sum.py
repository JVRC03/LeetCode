class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        jvrc = float('inf')

        def check(val, arr):
            for i in range(len(arr)):
                val += arr[i]

                if val < 1:
                    return False
            
            return True

        f, r = 1, 3000
        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, nums):
                jvrc = min(jvrc, mid)
                r = mid - 1
            else:
                f = mid + 1
        
        return jvrc
        