class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        jvrc = []

        def check(arr):
            for i in range(len(arr)):
                if len(arr[i]) and 0 <= int(arr[i]) <= 255:
                    if arr[i][0] == '0' and len(arr[i]) > 1:
                        return False
                    continue
                
                return False
            
            return True

        a = ''

        for i in range(len(s)):
            b = ''
            a += s[i]
            for j in range(i+1, len(s)):
                c = ''
                b += s[j]
                for k in range(j+1, len(s)):
                    d = ''
                    c += s[k]
                    for l in range(k+1, len(s)):
                        d += s[l]
                    if check([a, b, c, d]):
                        temp = a + '.' + b + '.' + c + '.' + d
                        jvrc.append(temp)

        return jvrc
        