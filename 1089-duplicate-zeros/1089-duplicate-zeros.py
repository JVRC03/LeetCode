class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        jvrc = []
        i = 0
        act=0

        while len(jvrc) < len(arr):
            if act:
                act = 0
                jvrc.append(0)
                continue
            if arr[i] != 0:
                jvrc.append(arr[i])
                i += 1
                continue

            jvrc.append(0)
            act = 1
            i += 1
        
        for i in range(len(arr)):
            arr[i] = jvrc[i]
            


        