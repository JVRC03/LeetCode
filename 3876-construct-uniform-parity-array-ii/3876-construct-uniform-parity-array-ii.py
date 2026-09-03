class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        odd, even = [], []
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
                if nums[i]%2 == 0:
                    even.append(nums[i])
                else:
                    odd.append(nums[i])

        odd.sort()
        even.sort()

        success = True
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                continue

            if odd[0] >= nums[i]:
                success = False
                break
        if success:
            return success

        for i in range(len(nums)):
            if nums[i]%2 == 1:
                continue
            if odd[0] >= nums[i]:
                return False

        return True

        