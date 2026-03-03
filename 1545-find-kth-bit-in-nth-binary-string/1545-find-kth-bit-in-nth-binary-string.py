class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        def rev(x):
            a = list(x)
            a = a[::-1]

            return ''.join(a)

        def inv(x):
            a = list(x)
            for i in range(len(a)):
                if a[i] == '0':
                    a[i] = '1'
                else:
                    a[i] = '0'

            return ''.join(a) 

        while k > len(s):
            temp = s + '1' + rev(inv(s))
            s = temp
        
        return s[k-1]
        