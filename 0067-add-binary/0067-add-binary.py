class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = abs(len(a) - len(b))

        s = '0' * diff

        if len(a) < len(b):
            a = s + a
        else:
            b = s + b
        
        jvrc = []

        a = list(a)
        b = list(b)

        while len(a) and len(b):
            c, d = a.pop(), b.pop()

            if c == d == '0':
                jvrc.append(c)
                continue
            
            if c != d:
                jvrc.append('1')
                continue
            
            jvrc.append('0')

            success = 0
            while len(a) and len(b):
                c, d = a.pop(), b.pop()

                if c == d == '0':
                    jvrc.append('1')
                    success = 1
                    break
                
                if c != d:
                    jvrc.append('0')
                    continue
                
                jvrc.append('1')
                            
            if not success:
                jvrc.append('1')
        
        jvrc = jvrc[::-1]
        return ''.join(jvrc)
            

        