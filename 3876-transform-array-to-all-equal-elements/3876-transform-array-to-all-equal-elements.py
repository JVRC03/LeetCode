class Solution:
    def canMakeEqual(self, arr: List[int], k: int) -> bool:

        def f(n, nums, p):
            for i in range(len(nums)-1):
                if nums[i] != n:
                    nums[i] = -nums[i] 
                    nums[i+1] = -nums[i+1]
                    p -= 1
                    if not p:
                        break
            
            if -n in nums:
                return 0
            
            return 1
        
        a = arr.copy()
        b = arr.copy()
       
        if f(-1, b, k) or f(1, a, k):
            return True
        
        return False
       