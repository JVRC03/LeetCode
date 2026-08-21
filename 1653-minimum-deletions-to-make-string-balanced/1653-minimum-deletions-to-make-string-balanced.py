class Solution:
    def minimumDeletions(self, s: str) -> int:
        arr = [s[0]]

        def func(arr):
            f, r = 0, len(arr) - 1
            idx = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] == 'a':
                    f = mid + 1
                else:
                    r = mid - 1
                    idx = mid

            return idx
            
        for i in range(1, len(s)):
            if arr[-1] == 'a':
                arr.append(s[i])
            else:
                if s[i] == 'b':
                    arr.append(s[i])
                else:
                    val = func(arr)
                    arr[val] = 'a'
        
        return len(s) - len(arr)