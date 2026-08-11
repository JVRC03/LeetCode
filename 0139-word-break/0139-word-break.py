class Solution:
    def wordBreak(self, s: str, kim: List[str]) -> bool:
        k = set(kim)
        self.jvrc = False

        dp = [-1] * len(s)

        def func(idx, s):
            if idx >= len(s) or self.jvrc:
                self.jvrc = True
                return True
        
            if dp[idx] != -1:
                return dp[idx]

            curr = ''
            glob = False

            for i in range(idx, len(s)):
                curr += s[i]
                if curr in k:
                    glob |= func(i + 1, s)
            
            dp[idx] = glob
            return dp[idx]

        func(0, s)
        return self.jvrc

        