class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dic = {}
        for i in range(len(s)):
            dic[i] = {}

        def check(s):
            if len(s) == 0:
                return 1
            if s[0] == '0':
                return 0
            
            if int(s) > 26:
                return 0
            
            return 1

        def func(idx, s, temp):
            if check(temp) == 0:
                return 0
            if idx >= len(s):
                if check(temp):
                    return 1
                return 0
            
            if temp in dic[idx]:
                return dic[idx][temp]

            one = func(idx + 1, s, s[idx])
            two = 0
            if idx + 1 < len(s):
                two = func(idx + 2, s, s[idx] + s[idx + 1])

            dic[idx][temp] = one + two
            return dic[idx][temp]

        return func(0, s, '')
        