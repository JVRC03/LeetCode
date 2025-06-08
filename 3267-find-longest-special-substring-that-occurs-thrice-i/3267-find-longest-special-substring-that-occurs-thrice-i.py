class Solution:
    def maximumLength(self, s: str) -> int:
        jvrc = -1
        def f(k):
            c = 0
            arr = []

            for i in range(len(k)):
                arr.append(s[i])
            
            if ''.join(arr) == k:
                c += 1
    
            for i in range(len(k), len(s)):
                arr.append(s[i])
                if ''.join(arr[i-len(k)+1:len(arr)]) == k:
                    c += 1
                if c >= 3:
                    return 1
            
            return 0

        for i in range(len(s)):
            temp = ''
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    break
                temp += s[j]
                if f(temp):
                    jvrc = max(jvrc, len(temp))

        return jvrc
                    
        