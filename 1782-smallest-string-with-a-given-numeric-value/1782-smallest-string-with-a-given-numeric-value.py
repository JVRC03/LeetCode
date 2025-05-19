class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        jvrc = ''
        for i in range(n):
            k -= 1
            jvrc += 'a'
        
        l = list(jvrc)
        r = 1

        while (k-25) >= 0:
            l[-r] = 'z'
            k -= 25
            r += 1

        if k:
            a = ord(l[-r])
            a += k
            l[-r] = chr(a)

        jvrc = ''.join(l)

        return jvrc 

        