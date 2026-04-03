class Solution:
    def finalPositionOfSnake(self, n: int, arr: List[str]) -> int:
        i, j = 0, 0

        for k in range(len(arr)):
            if arr[k] == 'UP':
                i -= 1
            elif arr[k] == 'DOWN':
                i += 1
            elif arr[k] == 'LEFT':
                j -= 1
            else:
                j += 1
        
        return (i * n) + j
        