class Solution:
    def mirrorFrequency(self, s: str) -> int:
        jvrc = 0
        alpha, nums = [(i+97) for i in range(25, -1, -1)], [i for i in range(9, -1, -1)]
        dic = {}
        num = {}

        for i in range(26):
            if i < 10:
                num[i] = 0
            
            dic[chr(i+97)] = 0

        for i in range(len(s)):
            if s[i].isalpha():
                dic[s[i]] += 1
                continue
            num[int(s[i])] += 1

        f, r = 0, 25
        while f < r:
            a = dic[chr(f+97)]
            b = dic[chr(r+97)]

            jvrc += abs(a - b)
            f += 1
            r -= 1
        
        f, r = 0, 9
        while f < r:
            a = num[f]
            b = num[r]

            jvrc += abs(a - b)
            f += 1
            r -= 1
       
        return jvrc
        