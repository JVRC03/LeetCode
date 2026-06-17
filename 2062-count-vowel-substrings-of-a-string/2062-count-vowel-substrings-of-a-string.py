class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        jvrc, vowels = 0, {'a', 'e', 'i', 'o', 'u'}
        f, r = 0, 0
        dic = {}

        def check(s):
            st = set()
            for i in range(len(s)):
                if s[i] not in vowels:
                    return 0
                st.add(s[i])
            
            if len(st) == 5:
                return 1
            
            return 0

        for i in range(len(s)):
            temp = ''
            for j in range(i, len(s)):
                temp += s[j]
                if check(temp):
                    jvrc += 1
        
        return jvrc
            

        