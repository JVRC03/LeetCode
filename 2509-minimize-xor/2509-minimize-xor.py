class Solution:
    def minimizeXor(self, n1: int, n2: int) -> int:
        c = 0

        while n2:
            if n2%2 == 1:
                c += 1
            n2 //= 2
        
        ss = ''
        while n1:
            ss += str(n1%2)

            n1 //= 2
        
        ss = ss[::-1]

        if len(ss) <= c:
            v = 0
            for i in range(c):
                n1 += int(math.pow(2, v))
                v += 1
            return n1
        
        s = ''

        for i in range(len(ss)):
            if ss[i] == '1':
                if c:
                    c -= 1
                    s += '1'
                else:
                    s += '0'
            else:
                s += '0'
        
        if c:
            l = list(s)
            for i in range(len(s)-1, -1, -1):
                if not c:
                    break
                if l[i] == '0':
                    l[i] = '1'
                    c -= 1
            s = ''.join(l)
        
        jvrc, v = 0, 0

        for i in range(len(s)-1, -1, -1):
            jvrc += (int(math.pow(2, v))*int(s[i]))
            v += 1
        
        return jvrc
                
        