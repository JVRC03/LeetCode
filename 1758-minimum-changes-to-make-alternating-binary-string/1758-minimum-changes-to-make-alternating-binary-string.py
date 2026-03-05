class Solution:
    def minOperations(self, s: str):
        a, b = 0, 0
        arr = list(s)

        for i in range(1, len(arr)):
            if arr[i-1] != arr[i]:
                continue
            
            if arr[i-1] == '1':
                arr[i] = '0'
            else:
                arr[i] = '1'
            a += 1

        arr = list(s)

        b = 1
        if arr[0] == '0':
            arr[0] = '1'
        else:
            arr[0] = '0'
        
        for i in range(1, len(arr)):
            if arr[i-1] != arr[i]:
                continue
            
            if arr[i-1] == '1':
                arr[i] = '0'
            else:
                arr[i] = '1'
            b += 1
        
        return min(a, b)
        