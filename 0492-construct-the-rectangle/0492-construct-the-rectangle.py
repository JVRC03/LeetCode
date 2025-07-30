class Solution:
    def constructRectangle(self, k: int) -> List[int]:
       
        jvrc = [k, 1]

        for i in range(1, (k//2)+2):
            a = k//i
            diff = abs(i-a)
            n = jvrc[0]-jvrc[-1]

            if i*a == k and diff < n:
                jvrc = [max(i, a), min(i, a)]
                
        return jvrc
        