class Solution:
    def bestClosingTime(self, s: str) -> int:
        p_sum = []
        if s[0] == 'Y':
            p_sum.append([0, 1])
        else:
            p_sum.append([1, 0])

        for i in range(1, len(s)):
            a, b = p_sum[-1][0], p_sum[-1][1]
            if s[i] == 'Y':
                b += 1
            else:
                a += 1
            p_sum.append([a, b])
        
        jvrc, tot = 0, p_sum[-1][-1]

        for i in range(1, len(s)):
            a = p_sum[i-1][0]
            b = p_sum[-1][-1]-p_sum[i-1][1]

            if a+b < tot:
                tot = a+b
                jvrc = i
        
        if p_sum[-1][0] < tot:
            jvrc = len(s)

        return jvrc


        