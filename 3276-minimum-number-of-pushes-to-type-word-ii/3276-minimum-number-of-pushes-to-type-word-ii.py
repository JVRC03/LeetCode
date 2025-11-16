class Solution:
    def minimumPushes(self, s: str) -> int:
        jvrc, dic = 0, {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        arr = list(dic.values())
        arr.sort()
        curr, k = 0, 1

        while len(arr):
            if curr == 8:
                k += 1
                curr = 0
            
            jvrc += (k * arr[-1])
            curr += 1
            arr.pop()
        
        return jvrc


        
        
        