class Solution:
    def validSubstringCount(self, s1: str, s2: str) -> int:
        dic = {}
        f, r = 0, 0
        temp = {}
        jvrc = 0

        for i in range(len(s2)):
            if s2[i] not in temp:
                temp[s2[i]] = 1
            else:
                temp[s2[i]] += 1

        def fa(dic):
            if len(dic) >= len(temp):
                for i in temp:
                    if i in dic and dic[i] >= temp[i]:
                        continue
                    return False
                return True
            return False

        while f <= r and r < len(s1):
            if s1[r] not in dic:
                dic[s1[r]] = 1
            else:
                dic[s1[r]] += 1
            
            if fa(dic):
                while f <= r and r < len(s1):
                    jvrc += (len(s1)-r)
                    dic[s1[f]] -= 1
                    if not dic[s1[f]]:
                        del dic[s1[f]]
                    f += 1
                    if fa(dic):
                        continue
                    break
            r += 1
        
        if fa(dic):
            while f <= r and r < len(s1):
                jvrc += (len(s1)-r)
                dic[s1[f]] -= 1
                if not dic[s1[f]]:
                    del dic[s1[f]]
                f += 1
                if fa(dic):
                    continue
                break
        
        return jvrc



        