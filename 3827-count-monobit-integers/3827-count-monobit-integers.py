class Solution:
    def countMonobit(self, n: int) -> int:
        jvrc = 1
        c = '1'
        while True:
            k = int(c, 2)
            if k <= n:
                jvrc += 1
                c += '1'
            else:
                break

        return jvrc
            
        