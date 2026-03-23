class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        jvrc = float('-inf')

        def check(idx, s, k, val):
            f = 0
            tot = 0

            for i in range(idx):
                if s[i] == val:
                    tot += 1
            
            rem = idx - tot

            if rem <= k:
                return True
            
            for i in range(idx, len(s)):
                if s[i] == val:
                    tot += 1
                if s[f] == val:
                    tot -= 1
                
                rem = idx - tot

                if rem <= k:
                    return True
                
                f += 1
            
            return False

        f, r = 0, len(s)
        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, s, k, 'T'):
                jvrc = max(jvrc, mid)
                f = mid + 1
            else:
                r = mid - 1
        
        f, r = 0, len(s)
        while f <= r:
            mid = f + ((r - f) // 2)

            if check(mid, s, k, 'F'):
                jvrc = max(jvrc, mid)
                f = mid + 1
            else:
                r = mid - 1

        return jvrc
        