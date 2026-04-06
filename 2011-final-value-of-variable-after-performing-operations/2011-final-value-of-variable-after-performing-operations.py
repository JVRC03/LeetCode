class Solution:
    def finalValueAfterOperations(self, arr: List[str]) -> int:
        jvrc = 0

        for i in range(len(arr)):
            if arr[i][0] == '-' or arr[i][-1] == '-':
                jvrc -= 1
            else:
                jvrc += 1
        
        return jvrc
        