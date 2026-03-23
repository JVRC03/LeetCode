class Solution:
    def platesBetweenCandles(self, s: str, q: List[List[int]]):  
        p_sum, arr = [], []
        cnt = 0

        for i in range(len(s)):
            if s[i] == '*':
                cnt += 1
            else:
                arr.append(i)
            p_sum.append(cnt)

        def check(low, high, arr, p_sum):

            f, r = 0, len(arr)-1
            a, b = -1, -1
            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] >= low:
                    a = mid
                    r = mid - 1
                else:
                    f = mid + 1
            
            f, r = 0, len(arr)-1
            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] > high:
                    r = mid-1
                else:
                    f = mid + 1
                    b = mid
            
            if a == -1 or b == -1:
                return 0
            
            f, r = 0, len(arr)-1
            while f <= r:
                mid = f + ((r - f) // 2)

                if low <= arr[mid] <= high:
                    return p_sum[arr[b]] - p_sum[arr[a]]
                
                if arr[mid] > high:
                    r = mid - 1
                else:
                    f = mid + 1

            return 0
            
        jvrc = []
        for i in range(len(q)):
            ans = check(q[i][0], q[i][1], arr, p_sum)
            jvrc.append(ans)

        return jvrc
        