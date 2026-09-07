class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = [nums[0]]
        def check(k):
            f, r = 0, len(arr) - 1

            ans = -1
            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] > k:
                    ans = mid
                    r = mid - 1
                else:
                    f = mid + 1

            return ans

        for i in range(1, len(nums)):
            val = check(nums[i])

            if val == -1:
                if arr[-1] != nums[i]:
                    arr.append(nums[i])
            else:
                temp = arr[val]
                arr[val] = nums[i]

                ori = len(arr)
                s = set(arr)

                if len(s) != ori:
                    arr[val] = temp
            
            if len(arr) > 2:
                return True
        
        return False
        
        