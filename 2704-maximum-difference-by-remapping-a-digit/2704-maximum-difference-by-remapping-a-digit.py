class Solution:
    def minMaxDifference(self, num: int) -> int:

        maxi, mini = -1, -1
        s = str(num)
        for i in range(len(s)):
            if s[i] != '9':
                maxi = s[i]
                break
        for i in range(len(s)):
            if s[i] != '0':
                mini = s[i]
                break
        
        if mini != -1 and maxi != -1:
            a, b = '', ''

            for i in range(len(s)):
                if s[i] == maxi:
                    a += '9'
                else:
                    a += s[i]
                
                if s[i] == mini:
                    b += '0'
                else:
                    b += s[i]
            return int (a)-int(b)
        

        if mini == -1:
            a = ''
            for i in range(len(s)):
                if s[i] == maxi:
                    a += '9'
                else:
                    a += s[i]
            return a
        
        a = ''

        for i in range(len(s)):
            if s[i] == mini:
                a += '0'
            else:
                a += s[i]
        
        return int(s)-int(a)
        