class Solution:
    def compareVersion(self, s1: str, s2: str) -> int:
        a, b = '', ''

        for i in range(len(s1)):
            if s1[i] == '0':
                if(len(a) == 0) or (a[-1] == '.'):
                    continue
                a += s1[i]
            else:
                a += s1[i]
        
        for i in range(len(s2)):
            if s2[i] == '0':
                if not len(b) or b[-1] == '.':
                    continue
                b += s2[i]
            else:
                b += s2[i]     

        def get(s):
            temp = ''
            arr = []
            for i in range(len(s)):
                if s[i] == '.':
                    if len(temp):
                        arr.append(int(temp))
                    else:
                        arr.append(0)
                    temp = ''
                else:
                    temp += s[i]
            
            if len(temp):
                arr.append(int(temp))
            else:
                arr.append(0)

            return arr

        jv = get(a)
        rc = get(b)

        i = 0

        while len(jv) and jv[-1] == 0:
            jv.pop()
            
        while len(rc) and rc[-1] == 0:
            rc.pop()

        while i < len(jv) and i < len(rc):
            if jv[i] == rc[i]:
                i += 1
                continue
            if jv[i] > rc[i]:
                return 1

            return -1
        
        if i == len(jv) and i == len(rc):
            return 0
        if i == len(jv):
            return -1

        return 1
  