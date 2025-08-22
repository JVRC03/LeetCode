class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        jvrc = 0
        arr = list(s)

        while True:
            c = 0
            i = 0

            while i < len(arr)-1:
                if arr[i] == '0' and arr[i+1] == '1':
                    c += 1
                    arr[i] = '1'
                    arr[i+1] = '0'
                    i += 1
                i += 1
            
            if not c:
                break
            
            jvrc += 1
        
        return jvrc

        