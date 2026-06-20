class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        jvrc = []
        for i in range(m):
            temp = ['#'] * n
            jvrc.append(temp)
        
        for i in range(m):
            jvrc[i][-1] = '.'
        
        for i in range(n):
            jvrc[0][i] = '.'
        
        jvrc1 = []
        for i in range(len(jvrc)):
            temp = ''.join(jvrc[i])
            jvrc1.append(temp)
            
        return jvrc1
        