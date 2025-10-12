class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, k: str) -> str:
        dic = {}
        jvrc = ''

        for i in range(len(s1)):
            stop = 0

            for j in dic:
                if j == s2[i] or s2[i] in dic[j] or s1[i] == j or s1[i] in dic[j]:
                    stop = 1
                    dic[j].add(s2[i])
                    dic[j].add(s1[i])
                    break

            if not stop:
                dic[s1[i]] = {s2[i]}

        real = {}
        stack = list(dic.keys())

        while len(stack):
            curr = stack.pop()
            if curr == -1:
                continue
            a = dic[curr]
            a.add(curr)
            del dic[curr]
            i = len(stack)-1

            while i > -1:
                if stack[i] != -1:
                    c = dic[stack[i]]
                    c.add(stack[i])
                    temp = a | c
                    if len(a) + len(c) != len(temp):
                        a = a|c
                        stack[i] = -1
                        i = len(stack)
                
                i -= 1
            
            real[curr] = a
        
        dic = real
       
        for i in range(len(k)):
            stop = 0
            for j in dic:
                if j == k[i] or k[i] in dic[j]:
                    p = min(list(dic[j]))
                    jvrc += (min(k[i], j, p)) 
                    stop = 1
                    break
            if not stop:
                jvrc += k[i]
        
        return jvrc
                

        