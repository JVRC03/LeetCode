class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd, even = {}, {}
        o, e = {}, {}

        for i in range(len(s1)):
            if i%2 == 0:
                if s1[i] not in even:
                    even[s1[i]] = 1
                else:
                    even[s1[i]] += 1
            else:
                if s1[i] not in odd:
                    odd[s1[i]] = 1
                else:
                    odd[s1[i]] += 1
            
            if i%2 == 0:
                if s2[i] not in e:
                    e[s2[i]] = 1
                else:
                    e[s2[i]] += 1
            else:
                if s2[i] not in o:
                    o[s2[i]] = 1
                else:
                    o[s2[i]] += 1
        
        for i in e:
            if i not in even or even[i] != e[i]:
                return False
        
        for i in even:
            if i not in e or e[i] != even[i]:
                return False
            
        for i in o:
            if i not in odd or odd[i] != o[i]:
                return False
        
        for i in odd:
            if i not in o or odd[i] != o[i]:
                return False
        
        return True


        