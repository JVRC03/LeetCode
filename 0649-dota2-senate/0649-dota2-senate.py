class Solution:
    def predictPartyVictory(self, s: str) -> str:
        r, d = [], []

        for i in range(len(s)):
            if s[i] == 'D':
                d.append(i)
            else:
                r.append(i)
        
        arr = list(s)
        i = 0
        while len(r) and len(d):
            if arr[i] == -1:
                i += 1
                if i == len(s):
                    i = 0
                continue
            
            if arr[i] == 'R':
                arr[d[0]] = -1
                k = r.pop(0)
                r.append(k)
                d.pop(0)

            else:
                arr[r[0]] = -1
                k = d.pop(0)
                d.append(k)
                r.pop(0)
                
            i += 1
            if i == len(s):
                i = 0
        
        if len(r):
            return 'Radiant'
        return 'Dire'
        