class Solution:
    def minOperations(self, s: str) -> int:
        se = set()

        for i in range(len(s)):
            if s[i] != 'a':
                se.add(s[i])

        arr = list(se)
        arr.sort()

        jvrc = 0

        for i in range(len(arr)-1):
            k = ord(arr[i+1])-ord(arr[i])
            jvrc += (k)
        
        if len(arr):
            k = (ord('z')-ord(arr[-1]))
            jvrc += (k+1)

        return jvrc
        