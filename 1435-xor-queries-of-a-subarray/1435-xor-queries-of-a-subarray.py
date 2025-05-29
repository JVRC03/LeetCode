class Solution:
    def xorQueries(self, jvrc: List[int], q: List[List[int]]) -> List[int]:
        p_sum = [jvrc[0]]

        for i in range(1, len(jvrc)):
            p_sum.append(p_sum[-1]^jvrc[i])
        
        jvrc = []

        for i in range(len(q)):
            if q[i][0] == 0:
                jvrc.append(p_sum[q[i][1]])
                continue
            a = bin(p_sum[q[i][1]])
            a = a[2:]

            b = bin(p_sum[q[i][0]-1])
            b = b[2:]
            n, c = 0, 0

            if len(b) > len(a):
                diff = len(b)-len(a)
                a = (diff*'0') + a

            if len(a) > len(b):
                diff = len(a)-len(b)
                b = (diff*'0') + b

            for j in range(len(b)-1, -1, -1):
                if (b[j] == '0' and a[j] == '0') or (b[j] == '1' and a[j] == '1'):
                    c += 1
                    continue
                n += int(math.pow(2, c))
                c += 1
            
            jvrc.append(n)
        
        return jvrc

                






        