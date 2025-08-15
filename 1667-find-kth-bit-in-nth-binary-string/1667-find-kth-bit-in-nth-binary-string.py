class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        while len(s) < k:
            temp = ''
            for i in range(len(s)):
                if s[i] == '0':
                    temp += '1'
                else:
                    temp += '0'
            
            temp = temp[::-1]
            s = s + '1' + temp
        
        return s[k-1]