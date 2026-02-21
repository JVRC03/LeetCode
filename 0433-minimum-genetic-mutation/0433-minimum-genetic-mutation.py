class Solution:
    def minMutation(self, src: str, k: str, word: List[str]) -> int:
        word = set(word)

        if k not in word:
            return -1

        jvrc = 0
        vis = {src}

        q = deque([src])

        while len(q):
            c = len(q)

            for i in range(c):
                s = q.popleft()
                lst = list(s)

                for l in range(len(s)):
                    for j in range(26):
                        lst[l] = chr(65 + j)

                        temp = ''.join(lst)

                        if temp not in vis:
                            if temp in word:
                                #print(q)
                                q.append(temp)
                                vis.add(temp)
                        
                        if temp == k and temp in word:
                            return jvrc + 1
                    
                    lst[l] = s[l]
            
            jvrc += 1
        
        return -1
                
        