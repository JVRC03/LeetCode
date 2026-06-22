class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        dic = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        jvrc = 0

        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
        
        while True:
            for i in dic:
                if i == 'l' or i == 'o':
                    dic[i] -= 2
                else:
                    dic[i] -= 1

                if dic[i] < 0:
                    return jvrc

            jvrc += 1


        