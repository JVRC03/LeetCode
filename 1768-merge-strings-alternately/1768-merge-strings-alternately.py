class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        f, r = 0, 0
        jvrc = ''

        while f < len(a) and r < len(b):
            jvrc += a[f]
            jvrc += b[r]
            r += 1
            f += 1
        
        while f < len(a):
            jvrc += a[f]
            f += 1
        
        while r < len(b):
            jvrc += b[r]
            r += 1
        
        return jvrc
        