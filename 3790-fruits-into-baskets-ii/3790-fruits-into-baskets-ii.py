class Solution:
    def numOfUnplacedFruits(self, arr: List[int], b: List[int]) -> int:
        jvrc = 0

        for i in range(len(arr)):
            c = 0
            for j in range(len(b)):
                if arr[i] <= b[j]:
                    b[j] = -1
                    c = 1
                    break
            if not c:
                jvrc += 1
        
        return jvrc
       