class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = max(len(a), len(b))-min(len(a), len(b))

        diff = '0' * temp

        if len(a) < len(b):
            a = diff+a
        elif len(b) < len(a):
            b = diff+b
        

        jvrc = ''
        i = len(a)-1

        while i >= 0:
            if a[i] == b[i] == '1':
                success = 1
                c = 0
                while i >= 0:
                    if a[i] == b[i] == '1':
                        if c:
                            jvrc += '1'
                        else:
                            jvrc += '0'
                        i -= 1
                        c = 1
                        continue
                    if a[i] == '1' or b[i] == '1':
                        jvrc += '0'
                        i -= 1
                        c = 1
                        continue
                    success = 0
                    jvrc += '1'
                    break        

                if success:
                    jvrc += '1'
                    break
            else:
                if a[i] == b[i] == '0':
                    jvrc += '0'
                else:
                    jvrc += '1'
            
            i -= 1
        
        return jvrc[::-1]