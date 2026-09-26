class Solution:
    def evaluate(self, s: str, arr: list[list[str]]) -> str:
        jvrc = ''
        dic = {}

        for i in range(len(arr)):
            dic[arr[i][0]] = arr[i][1]

        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                temp = ''
                while s[i] != ')':
                    temp += s[i]
                    i += 1
                if temp in dic:
                    jvrc += dic[temp]
                else:
                    jvrc += '?'
                i += 1
            else:
                jvrc += s[i]
                i += 1
        
        return jvrc
        


        