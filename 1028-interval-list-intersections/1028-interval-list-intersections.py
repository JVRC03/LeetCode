class Solution:
    def intervalIntersection(self, aa: List[List[int]], bb: List[List[int]]):
        jvrc = []

        def f(a, b):

            for i in range(len(b)):
                for j in range(len(a)):
                    if b[i][0] <= a[j][0] <= b[i][1]:
                        k = [  a[j][0], min(a[j][1], b[i][1])  ]
                        if k not in jvrc:
                            jvrc.append(k)
                    elif b[i][0] <= a[j][1] <= b[i][1]:
                        k = [  b[i][0], min(a[j][1], b[i][1])  ]
                        if k not in jvrc:
                            jvrc.append(k)

        f(aa, bb)
        f(bb, aa)
        jvrc.sort()
        return jvrc


        