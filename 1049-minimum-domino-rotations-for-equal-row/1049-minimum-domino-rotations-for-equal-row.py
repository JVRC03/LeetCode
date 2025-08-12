class Solution:
    def __init__(self):
        self.jvrc = float('inf')

    def minDominoRotations(self, aa: List[int], bb: List[int]) -> int:

        def f(a, b):
            dica, dicb = {}, {}

            for i in range(len(a)):
                if a[i] not in dica:
                    dica[a[i]] = [i]
                else:
                    dica[a[i]].append(i)

            for i in range(len(b)):
                if b[i] not in dicb:
                    dicb[b[i]] = set()
                    dicb[b[i]].add(i)
                else:
                    dicb[b[i]].add(i)

            for i in dica:
                if len(dica[i]) == len(a):
                    self.jvrc = 0
                    return 1
                if i not in dicb:
                    continue
                arr = dica[i]
                s = dicb[i]
                d = 0
                for j in range(len(arr)):
                    if arr[j] in s:
                        d += 1
                        s.remove(arr[j])

                if len(arr)+len(s)-d == len(a)-d:
                    self.jvrc = min(self.jvrc, len(s), len(arr)-d)
                    return 1
                return 0
        






        if f(aa, bb) or f(bb, aa):
            return self.jvrc
        
        return -1
  

        