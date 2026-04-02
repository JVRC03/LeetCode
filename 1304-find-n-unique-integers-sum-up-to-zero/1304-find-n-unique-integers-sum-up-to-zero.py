class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = n//2
        jvrc = []
        for i in range(1, k+1):
            jvrc.extend([i, -i])
        
        if n%2 == 1:
            jvrc.append(0)
        
        return jvrc
      