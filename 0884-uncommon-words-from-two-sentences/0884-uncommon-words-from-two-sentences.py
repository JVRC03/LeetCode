class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(' '), s2.split(' ')
        a, b = {}, {}

        for i in range(len(s1)):
            if s1[i] not in a:
                a[s1[i]] = 1
            else:
                a[s1[i]] += 1
        
        for i in range(len(s2)):
            if s2[i] not in b:
                b[s2[i]] = 1
            else:
                b[s2[i]] += 1
        
        jvrc = []
        for i in a:
            if i not in b and a[i] == 1:
                jvrc.append(i)
        
        for i in b:
            if i not in a and b[i] == 1:
                jvrc.append(i)
        
        return jvrc
        