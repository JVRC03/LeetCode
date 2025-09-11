class Solution:
    def sortVowels(self, s: str) -> str:
        arr = []
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(s)):
            if s[i] in v:
                arr.append(s[i])
        
        arr.sort()
        f = 0
        arr = arr[::-1]

        jvrc = ''

        for i in range(len(s)):
            if s[i] not in v:
                jvrc += s[i]
                continue
            jvrc += arr[-1]
            arr.pop()
        
        return jvrc
        
        