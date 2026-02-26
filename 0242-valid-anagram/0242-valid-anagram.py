class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = {}, {}

        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            else:
                a[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in b:
                b[t[i]] = 1
            else:
                b[t[i]] += 1
        
        if len(a) != len(b):
            return False
        
        while len(a):
            ele = -1

            for i in a:
                ele = i
                break
            
            if ele not in b:
                return False
            
            if b[ele] != a[ele]:
                return False
            
            del a[ele]
        
        return True
            
            
                 
        