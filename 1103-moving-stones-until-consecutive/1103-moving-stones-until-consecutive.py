class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        jvrc = [a, b, c]
        jvrc.sort()

        a = jvrc[0]
        b = jvrc[1]
        c = jvrc[2]

        f = b-a-1
        s = c-b-1
        jvrc = []

        if f > 1 and s > 1:
            jvrc = [2, (f+s)]
        else:
            if (f == 0 and s != 0) or (f != 0 and s == 0):
                jvrc = [1, (f+s)]
            else:
                if f == 1 or s == 1:
                    jvrc = [1, (f+s)]
                else:
                    jvrc = [0, (f+s)]
                
        return jvrc
        