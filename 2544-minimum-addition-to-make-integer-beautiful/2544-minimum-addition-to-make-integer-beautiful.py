class Solution:
    def makeIntegerBeautiful(self, n: int, k: int) -> int:

        def ok(s):
            c = 0
            for i in range(len(s)):
                c += int(s[i])
            
            if c <= k:
                return True
            return False
        
        jvrc = 0

        if ok(str(n)):
            return jvrc
        
        jvrc = 0
        c = 1
        
        while ok(str(n+jvrc)) == False:
            s = str(n)
            x = ''
            for i in range(len(s)-1, -1, -1):
                x += s[i]
                if len(x) == c:
                    break
            
            x = x[::-1]
            
            jvrc = (int(math.pow(10, c)))-int(x)
            c += 1

        return jvrc

        
     