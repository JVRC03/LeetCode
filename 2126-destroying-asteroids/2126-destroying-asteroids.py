class Solution:
    def asteroidsDestroyed(self, k: int, arr: List[int]) -> bool:
        arr.sort()

        for i in range(len(arr)):
            if k < arr[i]:
                return False
            k += arr[i]
        
        return True
        