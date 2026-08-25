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

        f = -1
        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] == 'b':
                    f = i
                stack.append(s[i])
                continue
            
            if stack[-1] == 'a':
                stack.append(s[i])
                if s[i] == 'b':
                    f = len(stack)-1
            else: 
                if s[i] == 'b':
                    stack.append(s[i])
                else: 
                    stack[f] = 'a'
                    f += 1

        return len(s) - len(stack)
        