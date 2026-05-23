class Solution:
    def check(self, nums: List[int]) -> bool:
        val, idx = float('inf'), []
        for i in range(len(nums)):
            if nums[i] < val:
                val = nums[i]
                idx = [i]
            else:
                idx.append(i)

        for h in range(len(idx)):
            curr = float('-inf')
            fail = False
            for i in range(len(nums)):
                if nums[(idx[h] + i) % len(nums)] >= curr:
                    curr = nums[(idx[h] + i) % len(nums)]
                    continue
                fail = True
                break
            if not fail:
                return True
            
        return False


        