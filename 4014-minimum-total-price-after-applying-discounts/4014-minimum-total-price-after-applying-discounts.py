class Solution:
    def minPrice(self, a: list[int], b: list[int]) -> float:
        a.sort()
        b.sort()
        jvrc = 0

        while len(b) and len(a):
            jvrc += a.pop() * (100 - b.pop()) / 100
        
        while len(a):
            jvrc += a.pop()
        
        return jvrc

        