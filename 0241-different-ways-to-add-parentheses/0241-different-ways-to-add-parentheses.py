class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        self.jvrc = []

        def func(i, j, s):
            if i > j:
                return [0]
            
            if i == j:
                return [int(s[i])]
            
            glob = []
            for k in range(i+1, j+1, 2):
                lp = func(i, k-1, s)
                rp = func(k+1, j, s)
                ans = []

                if s[k] == '*':
                    for x in range(len(lp)):
                        for y in range(len(rp)):
                            ans.append(lp[x] * rp[y])
                elif s[k] == '+':
                    for x in range(len(lp)):
                        for y in range(len(rp)):
                            ans.append(lp[x] + rp[y])
                else:
                    for x in range(len(lp)):
                        for y in range(len(rp)):
                            ans.append(lp[x] - rp[y])
            
                if i == 0 and j == len(s) - 1:
                    self.jvrc.extend(ans)
                
                glob.extend(ans)
            
            return glob

        arr = []
        temp = ''
        for i in range(len(s)):
            if s[i] not in {'+', '*', '-'}:
                temp += s[i]
                continue
            
            arr.append(temp)
            arr.append(s[i])
            temp = ''
        
        if len(temp):
            arr.append(temp)
        
        func(0, len(arr) - 1, arr)
        if len(self.jvrc) == 0:
            return [int(s)]
        return self.jvrc
        