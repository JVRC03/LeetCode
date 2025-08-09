class Solution:
    def minAnagramLength(self, s: str) -> int:

        def naa_istam(a, b):
            for i in a:
                if i not in b or a[i] != b[i]:
                    return False
            
            return True
        
        def f(x, dic):
            for i in range(0, len(s), len(x)):
                temp = {}
                for j in range(len(x)):
                    if s[i+j] not in temp:
                        temp[s[i+j]] = 1
                    else:
                        temp[s[i+j]] += 1
                
                if len(temp) != len(dic):
                    return False
                
                if naa_istam(temp, dic) == False:
                    return False
                    
            return True

        c = {}
        temp = ''
        for i in range(len(s)):
            temp += s[i]

            if s[i] not in c:
                c[s[i]] = 1
            else:
                c[s[i]] += 1

            if len(s)%len(temp) == 0:
                if f(temp, c):
                    return len(temp)

        return len(s)
       