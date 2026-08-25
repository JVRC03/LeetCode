class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        stack = []
        def check(a):
            f, r = 0, len(stack) - 1
            ans = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if stack[mid] <= a:
                    f = mid + 1
                else:
                    ans = mid
                    r = mid - 1
            
            return ans

        for i in range(len(s)):
            val = check(s[i])

            if val == -1:
                stack.append(s[i])
            else:
                stack[val] = s[i]
    
        return len(s) - len(stack)
        