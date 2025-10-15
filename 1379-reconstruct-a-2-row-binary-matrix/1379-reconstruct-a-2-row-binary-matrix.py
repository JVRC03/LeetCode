class Solution:
    def reconstructMatrix(self, a: int, b: int, arr: List[int]) -> List[List[int]]:
        if a+b != sum(arr):
            return []
        
        jvrc = []
        for i in range(2):
            temp = [-1] * len(arr)
            jvrc.append(temp)
        
        for i in range(len(arr)):
            if arr[i] == 0:
                jvrc[0][i] = 0
                jvrc[1][i] = 0
            elif arr[i] == 2:
                jvrc[0][i] = 1
                jvrc[1][i] = 1
                a -= 1
                b -= 1

        for i in range(len(arr)):
            if jvrc[0][i] == -1:
                if a:
                    jvrc[0][i] = 1
                    a -= 1
                    jvrc[1][i] = 0
                else:
                    jvrc[0][i] = 0
                    jvrc[1][i] = 1
                    b -= 1
        
        if a == 0 and b == 0:
            return jvrc
        
        return []


            

        