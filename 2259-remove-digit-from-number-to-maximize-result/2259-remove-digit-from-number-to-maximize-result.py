class Solution:
    def removeDigit(self, s: str, k: str) -> str:
        
        def func(arr, k):
            jvrc = ''

            for i in range(len(arr)):
                if arr[i] == k:
                    arr[i] = ''
                    jvrc = max(jvrc, ''.join(arr))
                    arr[i] = k
            return jvrc
        
        return func(list(s), k)
        