class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = []

        for i in range(65):
            arr.append(int(math.pow(2, i)))
        
        b = str(n)
        b = list(b)
        b.sort()
        b = ''.join(b)

        for i in range(len(arr)):
            a = str(arr[i])
            a = list(a)
            a.sort()
            a = ''.join(a)
            
            if a == b:
                return True
        
        return False



        