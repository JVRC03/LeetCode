class Solution:
    def largestCombination(self, arr: List[int]) -> int:
        dic = {}

        for i in range(len(arr)):
            s = bin(arr[i])
            s = s[2:]
            c = 0
            for j in range(len(s)-1, -1, -1):
                if s[j] == '1':
                    if c not in dic:
                        dic[c] = 1
                    else:
                        dic[c] += 1
                c += 1
                
        jvrc = 0

        for i in dic:
            jvrc = max(jvrc, dic[i])

        return jvrc
        