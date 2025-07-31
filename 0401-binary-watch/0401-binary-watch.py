class Solution:

    def __init__(self):
        self.jvrc = set()
    
    def left(self, arr):
        x = [1, 2, 4, 8]
        c = 0

        for i in range(len(arr)):
            if arr[i]:
                c += x[i]

        if c > 11:
            return ''   

        return str(c)

    def right(self, arr):
        x = [1, 2, 4, 8, 16, 32]
        c = 0
        for i in range(len(arr)):
            if arr[i]:
                c += x[i]

        if c > 59:
            return ''  
        
        if c < 10:
            return '0'+str(c)

        return str(c)
    
    def f(self, k, arr, v):
 
        if v == k:
            l = self.left(arr[0:4])
            r = self.right(arr[4:])
            
            if len(l) > 0 and len(r) > 0:
                s = l + ':' + r
                
                if s not in self.jvrc:
                    self.jvrc.add(s)
            return  
        
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = 1
                v += 1
                self.f(k, arr, v)
                v -= 1
                arr[i] = 0

    def readBinaryWatch(self, k: int) -> List[str]:
        if k > 8:
            return []

        arr = [0] * 10
        self.f(k, arr, 0)

        return list(self.jvrc)
        