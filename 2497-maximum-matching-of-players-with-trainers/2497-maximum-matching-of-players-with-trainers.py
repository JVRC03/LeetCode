class Solution:
    def matchPlayersAndTrainers(self, a: List[int], b: List[int]) -> int:
        f, r = 0, 0
        jvrc = 0
        a.sort()
        b.sort()

        while f < len(a) and r < len(b):
            if a[f] <= b[r]:
                jvrc += 1
                f += 1
                r += 1
                continue
            r += 1
        
        return jvrc
        