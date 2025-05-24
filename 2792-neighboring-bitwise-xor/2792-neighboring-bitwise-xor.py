class Solution:
    def doesValidArrayExist(self, arr: List[int]) -> bool:
        
        def f(jvrc):
            for i in range(len(arr)-1):
                if arr[i] == 1:
                    if jvrc[-1] == 0:
                        jvrc.append(1)
                    else:
                        jvrc.append(0)
                else:
                    if jvrc[-1] == 0:
                        jvrc.append(0)
                    else:
                        jvrc.append(1)
            
            if jvrc[-1]^jvrc[0] == arr[-1]:
                return True
        
        if f([0]) or f([1]):
            return True

        return False





        