class Solution:
    def originalDigits(self, s: str) -> str:
        arr = ['z', 'w', 'x', 'u', 'g', 'r', 'f', 'v', 'o', 'n']
        ans = ['zero', 'two', 'six', 'four', 'eight', 'three', 'five', 'seven', 'one', 'nine']
        num = [0, 2, 6, 4, 8, 3, 5, 7, 1, 9]

        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        jvrc = []

        while len(dic):
            for i in range(len(arr)):
                if arr[i] in dic:
                    for j in range(len(ans[i])):
                        dic[ans[i][j]] -= 1
                        if not dic[ans[i][j]]:
                            del dic[ans[i][j]]
                    jvrc.append(str(num[i]))
                    break
        
        jvrc.sort()

        return ''.join(jvrc)


        