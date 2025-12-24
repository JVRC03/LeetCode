class Solution:
    def minimumBoxes(self, b: List[int], a: List[int]) -> int:
        a.sort()
        k = sum(b)
        jvrc = 1

        while True:
            c = a.pop()
            k -= c
            if k <= 0:
                break
            jvrc += 1
        
        return jvrc

            

        