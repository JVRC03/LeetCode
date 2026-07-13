class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = len(str(low))
        h = len(str(high))

        jvrc = set()

        for i in range(l, h+1):
            for j in range(1, 10):
                s = ''
                for k in range(0, 10):
                    if j + k >= 10:
                        break
                    s += str(j + k)
                    if low <= int(s) <= high and l <= len(s) <= h:
                        jvrc.add(int(s))
        

        jvrc = list(jvrc)
        jvrc.sort()
        return jvrc
        