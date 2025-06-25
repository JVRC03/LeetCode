class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        jvrc = 0

        def f(a, b):
            c = 0

            for i in range(len(a)):
                if a[i] != b[i]:
                    if c:
                        return False
                    c += 1
                    continue
                continue

            if c == 1:
                return True
            return False

        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                temp.append(s[j])
                arr = []
                if len(temp) > len(t):
                    break
                for k in range(len(temp)):
                    arr.append(t[k])

                sf = ''.join(arr)
                if f(sf, ''.join(temp)):
                    jvrc += 1
                    
                for k in range(len(temp), len(t)):
                    arr.pop(0)
                    arr.append(t[k])
                    sf = ''.join(arr)
                    if f(sf, ''.join(temp)):
                        jvrc += 1
        
        return jvrc
                    
        