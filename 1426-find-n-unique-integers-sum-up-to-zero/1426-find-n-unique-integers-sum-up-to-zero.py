class Solution:
    def sumZero(self, n: int) -> List[int]:
        jvrc = []
        if n%2 == 1:
            jvrc.append(0)
            n -= 1
        c = 1

        while n:
            jvrc.append(c)
            jvrc.append(-c)
            n -= 2
            c += 1

        return jvrc
        