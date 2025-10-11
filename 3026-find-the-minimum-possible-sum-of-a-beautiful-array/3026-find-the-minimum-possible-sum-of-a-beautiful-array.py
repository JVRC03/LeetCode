class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        if n < target//2:
            return ((n * (n+1))//2)%1000000007
            
        k = target//2
        jvrc = (k * (k+1))//2

        n -= k
        rem = target+n-1
        tot =  (rem * (rem+1))//2

        c = target-1

        waste = (c * (c+1))//2

        jvrc += (tot-waste)

        return jvrc%1000000007


        