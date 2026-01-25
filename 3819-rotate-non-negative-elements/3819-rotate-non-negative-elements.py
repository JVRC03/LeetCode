class Solution:
    def rotateElements(self, jvrc: List[int], k: int) -> List[int]:
        arr = []

        for i in range(len(jvrc)):
            if jvrc[i] >= 0:
                arr.append(jvrc[i])
                continue
        
        if not len(arr):
            return jvrc
        idx = k%len(arr)

        for i in range(len(jvrc)):
            if jvrc[i] < 0:
                continue
            
            jvrc[i] = arr[idx]

            idx = (idx + 1)%len(arr)
        
        return jvrc


        