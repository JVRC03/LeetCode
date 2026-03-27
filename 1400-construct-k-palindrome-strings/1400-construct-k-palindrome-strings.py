class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        
        if len(s) < k:
            return False
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        while k:
            found = False

            for i in dic:
                if dic[i]%2 == 1:
                    dic[i] -= 1
                    k -= 1
                    if not dic[i]:
                        del dic[i]
                    found = True
                    break

            if not found:
                break
        
        c = 0
        for i in dic:
            
            if dic[i]%2 == 1:
                c += 1
            
            if c > 1:
                return False
        
        if not k and c:
            return False

        return True