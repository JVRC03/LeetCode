class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        jvrc = 0

        z, o = 0, 0
        arr = []

        for i in range(len(s)):
            if s[i] == '0':
                z += 1
                if o:
                    arr.append(o)
                    o = 0
            else:
                o += 1
                if z:
                    arr.append(z)
                    z = 0

        if z:
            arr.append(z)
        if o:
            arr.append(o)
        
        for i in range(len(arr)-1):
            k = min(arr[i], arr[i+1])
            jvrc += k
        
        return jvrc
                


        