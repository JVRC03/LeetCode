class Solution:
    def nextGreatestLetter(self, arr: List[str], k: str) -> str:

        def f(arr, k):
            low, high = 0, len(arr)-1
            ans = -1

            while low <= high:
                mid = low + ((high - low) // 2)

                if arr[mid] > k:
                    ans = arr[mid]
                    high = mid-1
                else:
                    low = mid+1
            
            return ans
        
        jvrc = f(arr, k)

        if jvrc == -1:
            return arr[0]
        
        return jvrc

        