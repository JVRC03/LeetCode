class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return (r - l) + 1
        jvrc = 0
        c, curr = int(math.pow(l, 1 / k)) - 1, 0
        if c < 0:
            c = 0

        while True:
            if curr > r:
                break
            
            curr = int(math.pow(c, k))
            c += 1

            if l <= curr <= r:
                jvrc += 1
        
        return jvrc


        