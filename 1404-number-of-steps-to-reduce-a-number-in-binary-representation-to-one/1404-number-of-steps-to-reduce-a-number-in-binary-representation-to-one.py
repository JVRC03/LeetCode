class Solution:
    def numSteps(self, s: str) -> int:
        arr = list(s)
        jvrc = 0

        while len(arr) > 1:
            while len(arr) and arr[-1] == '0':
                jvrc += 1
                arr.pop()
            
            if len(arr) <= 1:
                continue

            c = 0

            for i in range(len(arr)-1, -1, -1):
                if arr[i] == '1':
                    arr[i] = '0'
                    c += 1
                else:
                    arr[i] = '1'
                    break
            
            if c == len(arr):
                arr.insert(0, '1')
            
            jvrc += 1
        
        return jvrc
            
        