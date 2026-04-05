class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        tot = int(n**(1/3)) + 1
        jvrc = []
        dic = {}

        for i in range(1, tot):
            for j in range(i, tot):
                a = i**3
                b = j**3

                k = a + b
                if k > n:
                    continue

                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1
        
        for i in dic:
            if dic[i] > 1:
                jvrc.append(i)
        jvrc.sort()
        return jvrc
        