class Solution:
    def intToRoman(self, num: int) -> str:
        u = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        t = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        h = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        to = ['', 'M', 'MM', 'MMM']

        k = str(num)

        diff = 4 - len(k)

        k = (diff * '0') + k

        jvrc = to[int(k[0])] + h[int(k[1])] + t[int(k[2])] + u[int(k[3])]
        
        return jvrc
        