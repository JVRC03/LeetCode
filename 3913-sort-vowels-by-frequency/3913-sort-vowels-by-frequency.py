class Solution:
    def sortVowels(self, s: str) -> str:
        dic = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(len(s)):
            if s[i] in vowels:
                if s[i] not in dic:
                    dic[s[i]] = 1
                else:
                    dic[s[i]] += 1
        
        arr = []

        def get(dic):
            key, val = -1, -1
            for i in dic:
                if val < dic[i]:
                    val = dic[i]
                    key = i

            del dic[key]

            return key, val, dic 
            
        while len(dic):
            key, val, dic = get(dic)
            arr.append([key, val])
        
        arr = arr[::-1]

        jvrc = ''
        for i in range(len(s)):
            if s[i] in vowels:
                jvrc += arr[-1][0]
                arr[-1][1] -= 1
                if not arr[-1][1]:
                    arr.pop()
            else:
                jvrc += s[i]
        
        return jvrc
        