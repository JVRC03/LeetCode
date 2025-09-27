class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def get_primes(x):
            temp = [1] * (x+1)
            temp[0] = 0
            temp[1] = 0
            v = []

            for i in range(2, int(math.sqrt(x))+1):
                c = 2*i
                for j in range(c, x+1, i):
                    temp[j] = 0
            
            for i in range(len(temp)):
                if temp[i]:
                    v.append(i)
            
            return v
        
        def get_min(arr, k):
            f, r = 0, len(arr)-1
            idx = -1

            while f <= r:
                mid = (f+r)//2

                if arr[mid] > k:
                    r = mid-1
                else:
                    idx = max(idx, mid)
                    f = mid+1
            
            return idx
        
        def get_mini(arr, k):
            ans = -1
            for i in range(len(arr)):
                if arr[i] < k:
                    ans = i
                    continue
                break
            return ans

        arr = get_primes(max(nums))

        for i in range(len(nums)):
            k = -1
            if i-1>=0:
                if nums[i] <= nums[i-1]:
                    return False
                k = get_min(arr, nums[i]-nums[i-1]-1)
            else:
                k = get_mini(arr, nums[i])

            if k != -1:
                nums[i] -= arr[k] 
        
        if len(nums) > 1 and nums[-1] <= nums[-2]:
            return False
        
        return True
                    

            



        

        