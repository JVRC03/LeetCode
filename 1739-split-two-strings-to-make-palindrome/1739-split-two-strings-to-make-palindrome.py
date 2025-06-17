class Solution:
    def checkPalindromeFormation(self, aa: str, bb: str) -> bool:
        if (aa == aa[::-1]) or (bb == bb[::-1]):
            return True
        

        def ff(x, y, a):
            while x <= y:
                if a[x] != a[y]:
                    return False
                x += 1
                y -= 1
            
            return True

        def f(a, b):
            f, r = 0, len(a)

            if len(a)%2 == 1:
                f = 1
                
            for i in range(len(a)):
                if a[i] == b[len(a)-i-1]:
                    f += 1
                    r -= 1
                    if f == r:
                        return True
                    continue
                elif ff(i, len(a)-i-1, b) == True or ff(i, len(a)-i-1, a) == True:
                    return True
                return False
        
        if f(aa, bb) or f(bb, aa):
            return True
        
        return False
        