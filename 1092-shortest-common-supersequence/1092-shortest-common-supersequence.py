class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        s1, s2 = s2, s1
        dp = []
        for i in range(len(s1) + 1):
            dp.append([0] * (len(s2) + 1))
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        jvrc = ''
        f, r = len(s1), len(s2)

        while f > 0 and r > 0:
            if dp[f][r - 1] > dp[f - 1][r]:
                jvrc += s2[r - 1]
                r -= 1
            elif dp[f][r - 1] < dp[f - 1][r]:
                jvrc += s1[f - 1]
                f -= 1
            else:
                if s1[f - 1] == s2[r - 1]:
                    jvrc += s1[f - 1]
                    f -= 1
                    r -= 1
                else:
                    jvrc += s1[f - 1]
                    f -= 1
        
        while f > 0:
            jvrc += s1[f - 1]
            f -= 1
        
        while r > 0:
            jvrc += s2[r - 1]
            r -= 1

        return jvrc[::-1]



        