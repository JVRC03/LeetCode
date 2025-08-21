class Solution:
    def placeWordInCrossword(self, mat: List[List[str]], k: str) -> bool:

        def f(s, k):
            for i in range(len(s)):
                if s[i] == ' ':
                    continue
                if s[i] != k[i]:
                    return False
            
            return True

        for i in range(len(mat[0])):
            s = ''
            for j in range(len(mat)):
                if mat[j][i] != '#':
                    s += mat[j][i]
                    continue

                if len(s) != len(k):
                    s = ''
                    continue

                if f(s, k) or f(s[::-1], k):
                    return True

                s = '' 
            
            if len(s) == len(k) and (f(s, k) or f(s[::-1], k)):
                return True 
        
        for i in range(len(mat)):
            s = ''
            for j in range(len(mat[0])):
                if mat[i][j] != '#':
                    s += mat[i][j]
                    continue

                if len(s) != len(k):
                    s = ''
                    continue

                if f(s, k) or f(s[::-1], k):
                    return True

                s = '' 

            if len(s) == len(k) and (f(s, k) or f(s[::-1], k)):
                return True 
        
        return False
                

        