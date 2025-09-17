class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [1] * (n)

        arr[0] = 0
        arr[1] = 0

        a = int(math.sqrt(n))+1

        for i in range(2, a):
            c = i*2
            for j in range(c, len(arr), i):
                arr[j] = 0
        
        return arr.count(1)
        