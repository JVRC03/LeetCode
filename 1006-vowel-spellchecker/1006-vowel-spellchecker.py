class Solution:
    def spellchecker(self, a: List[str], jvrc: List[str]) -> List[str]:
        s = set(a)
        dic, v = {}, {}
        vo = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(a)):
            temp = a[i].lower()
            if temp not in dic:
                dic[temp] = i
            temp = ''
            for j in range(len(a[i])):
                if a[i][j] in vo:
                    temp += '-'
                    continue
                temp += a[i][j].lower()

            if temp not in v:
                v[temp] = i

        for i in range(len(jvrc)):
            if jvrc[i] in s:
                continue

            temp = jvrc[i].lower()

            if temp in dic:
                jvrc[i] = a[dic[temp]]
                continue

            temp = ''

            for j in range(len(jvrc[i])):
                if jvrc[i][j] in vo:
                    temp += '-'
                    continue
                temp += jvrc[i][j].lower()
            
            if temp in v:
                jvrc[i] = a[v[temp]]
                continue
            
            jvrc[i] = ''
        
        return jvrc
                        


        