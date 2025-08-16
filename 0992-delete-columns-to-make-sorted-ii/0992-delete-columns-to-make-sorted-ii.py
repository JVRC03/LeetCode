class Solution:
    def minDeletionSize(self, arr: List[str]) -> int:
        jvrc = 0

        while True:
            stop = 0
            idx = -1

            for i in range(len(arr)-1):
                if arr[i] <= arr[i+1]:
                    continue
                idx = i
                stop = 1
                break
            
            if not stop:
                break
            
            inner_idx = -1
            a, b = arr[i], arr[i+1]

            for i in range(len(a)):
                if a[i] > b[i]:
                    inner_idx = i
                    break
            for i in range(len(arr)):
                s = list(arr[i])
                s.pop(inner_idx)
                arr[i] = ''.join(s)
            jvrc += 1

        return jvrc
            

            


        