class Solution:
    def minimumOperationsToMakeKPeriodic(self, s: str, k: int) -> int:
        temp = ''
        i, jvrc = 0, 0
        dic = {}
        
        while i < len(s):
            temp += s[i]
            i += 1

            if len(temp) == k:
                if temp not in dic:
                    dic[temp] = 1
                else:
                    dic[temp] += 1
            
                jvrc = max(jvrc, dic[temp])
                temp = ''
        
        return (len(s)//k)-jvrc
        