class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        r = len(arr)-1

        while r >= 0:
            if arr[r] != 9:
                arr[r] += 1
                break
            
            arr[r] = 0
            r -= 1
        
        if r < 0:
            arr[0] = 1
            arr.append(0)
        
        return arr

        