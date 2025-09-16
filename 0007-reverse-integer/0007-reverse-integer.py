class Solution:
    def reverse(self, x: int) -> int:
        k = str(abs(x))
        jvrc = int(k[::-1])

        if -int(math.pow(2, 31)) <= jvrc <= int(math.pow(2, 31)):

            if x < 0:
                return -jvrc
            
            return jvrc
        
        return 0

        