class Solution:
    def reverseVowels(self, s: str) -> str:
        jvrc = list(s)
        f, r = 0, len(s)-1
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while f < r:
            if jvrc[f] in v and jvrc[r] in v:
                jvrc[f], jvrc[r] = jvrc[r], jvrc[f]
                f += 1
                r -= 1
                continue
            
            if jvrc[f] in v:
                r -= 1
            elif jvrc[r] in v:
                f += 1
            else:
                f += 1
                r -= 1
        
        return ''.join(jvrc)
        