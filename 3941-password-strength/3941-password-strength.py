class Solution:
    def passwordStrength(self, s: str) -> int:
        dic = {
            'l' : set(), 
            'u' : set(),
            'd' : set(),
            's' : set(),
        }

        for i in range(len(s)):
            if s[i].islower():
                dic['l'].add(s[i])
            elif s[i].isupper():
                dic['u'].add(s[i])
            elif s[i].isdigit():
                dic['d'].add(s[i])
            else:
                dic['s'].add(s[i])
        
        return len(dic['l']) + (2 * len(dic['u'])) + (3 * len(dic['d'])) + (5 * len(dic['s']))
        