class Solution:
    def minimumPerimeter(self, key: int) -> int:
        f, r = 2, 100000
        side = float('inf')

        def check(n, key):
            n -= 1
            x_sum, y_sum, mid, total = 0, 0, 0, 0

            x_sum = ((n * (n+1))//2) * n
            y_sum = ((n * (n+1))//2) * n

            part = (x_sum + y_sum) * 4

            mid = ((n * (n+1))//2) * 4

            total = part + mid

            if total >= key:
                return True
        
            return False

        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, key):
                side = min(side, mid)
                r = mid-1
            else:
                f = mid+1
        
        return 8 * (side-1)

        
        