class Solution:
    def executeInstructions(self, n: int, jvrc: List[int], s: str) -> List[int]:
        ud, lr = jvrc[0], jvrc[1]
        a, b = ud, lr
        jvrc.pop()
        jvrc.pop()

        for i in range(len(s)):
            c = 0
            ud, lr = a, b
            for j in range(i, len(s)):
                if s[j] == 'R' or s[j] == 'L':
                    if s[j] == 'R':
                        if lr+1 < n:
                            lr += 1
                            c += 1
                            continue
                        break
                    if lr-1 >= 0:
                        lr -= 1
                        c += 1
                        continue
                    break
                else:
                    if s[j] == 'D':
                        if ud+1 < n:
                            ud += 1
                            c += 1
                            continue
                        break
                    if ud-1 >= 0:
                        ud -= 1
                        c += 1
                        continue
                    break
            jvrc.append(c)
        
        return jvrc


                
        