class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        f, r = 0, 0
        jvrc = 0
        dic = {}

        while f <= r and r < len(s):
            if s[r] in {'a', 'b', 'c'}:
                if s[r] not in dic:
                    dic[s[r]] = 1
                else:
                    dic[s[r]] += 1
            
            while len(dic) == 3:
                jvrc += (len(s) - r)
                if s[f] in dic:
                    dic[s[f]] -= 1
                    if not dic[s[f]]:
                        del dic[s[f]]
                f += 1
            
            r += 1
        
        return jvrc



        