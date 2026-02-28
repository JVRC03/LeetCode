class Solution:
    def concatenatedBinary(self, n: int) -> int:
        jvrc = 0
        curr = 1

        for i in range(n, 0, -1):
            k = bin(i)
            k = k[2:]

            for j in range(len(k)-1, -1, -1):
                
                if k[j] == '1':
                    jvrc += curr
                curr *= 2
                curr %= 1000000007
    
        return jvrc%1000000007
        

        