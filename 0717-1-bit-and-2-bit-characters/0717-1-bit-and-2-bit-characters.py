class Solution:
    def isOneBitCharacter(self, arr: List[int]) -> bool:
        arr.pop()
        i = 0

        while i < len(arr):
            if arr[i] == 0:
                i += 1
                continue
            
            if i+1 < len(arr):
                i += 1
            else:
                return False
            
            i += 1
        
        return True

        