class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        jvrc = []

        temp = [1] * (n+1)

        for i in range(2, len(temp)):
            c = i*i
            for j in range(c, len(temp), i):
                temp[j] = 0
        
        for i in range(1, (n//2)+1):
            if temp[i] and i > 1:
                if temp[n-i]:
                    jvrc.append([i, (n-i)])

        return jvrc
        