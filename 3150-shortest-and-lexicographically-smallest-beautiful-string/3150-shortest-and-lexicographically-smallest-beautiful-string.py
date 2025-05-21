class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        jvrc = ''
        arr = []

        for i in range(len(s)):
            if s[i] == '1':
                arr.append(i)
        
        if len(arr) < k:
            return jvrc
        
        for i in range(1+len(arr)-k):
            temp = s[arr[i]:arr[i+k-1]+1]
            if not len(jvrc):
                jvrc = temp
                continue
            
            if len(temp) < len(jvrc):
                jvrc = temp
            elif len(temp) == len(jvrc):
                jvrc = min(jvrc, temp)

        return jvrc

        