class Solution:
    def intToRoman(self, num: int) -> str:
        u = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        t = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        h = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

        jvrc = ''

        k = str(num)

        if len(k) == 4:
            jvrc += (int(k[0]) * 'M')
            if k[1] != '0':
                jvrc += (h[int(k[1]) - 1])
            if k[2] != '0':
                jvrc += (t[int(k[2]) - 1])
            if k[3] != '0':
                jvrc += (u[int(k[3]) - 1])
        
        elif len(k) == 3:
            jvrc += (h[int(k[0]) - 1])
            if k[1] != '0':
                jvrc += (t[int(k[1]) - 1])
            if k[2] != '0':
                jvrc += (u[int(k[2]) - 1])
        
        elif len(k) == 2:
            jvrc += (t[int(k[0]) - 1])
            if k[1] != '0':
                jvrc += (u[int(k[1]) - 1])

        else:
            jvrc += (u[int(k[0]) - 1])
        
        return jvrc
        