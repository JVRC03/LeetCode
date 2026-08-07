class Solution:
    def recoverOrder(self, a: List[int], b: List[int]) -> List[int]:
        s = set(b)
        f = 0

        for i in range(len(a)):
            if f == len(b):
                break
            if a[i] in s:
                b[f] = a[i]
                f += 1
        
        return b
        