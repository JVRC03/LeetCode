class Solution:
    def getDescentPeriods(self, arr: List[int]) -> int:
        f, r = 0, 1
        jvrc = len(arr)

        while f < r and r < len(arr):
            if arr[r]+1 == arr[r-1]:
                r += 1
                continue
            
            n = r-f-1
            jvrc += ((n * (n+1))//2)

            f = r
            r += 1

        n = r-f-1
        jvrc += ((n * (n+1))//2)

        return jvrc

        

        