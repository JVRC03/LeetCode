class Solution:
    def findOcurrences(self, s: str, a: str, b: str):
        arr = s.split(' ')
        jvrc = []
        i = 0

        while i < len(arr):
            if arr[i] == a:
                if i+1 < len(arr):
                    if arr[i+1] == b:
                        if i+2 < len(arr):
                            jvrc.append(arr[i+2])
                                      
            i += 1
        
        return jvrc



        