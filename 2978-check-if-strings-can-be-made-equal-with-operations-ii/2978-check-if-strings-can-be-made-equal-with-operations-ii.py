class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        dic = {0 : [], 1 : [], 2 : [], 3 : []}

        for i in range(len(s1)):
            if i%2 == 0:
                dic[0].append(s1[i])
                dic[2].append(s2[i])
            else:
                dic[1].append(s1[i])
                dic[3].append(s2[i])
        

        dic[0].sort()
        dic[1].sort()
        dic[2].sort()
        dic[3].sort()
        
        j = ''.join(dic[0])
        r = ''.join(dic[1])
        v = ''.join(dic[2])
        c = ''.join(dic[3])

        if j == v and r == c:
            return True
        
        return False
        