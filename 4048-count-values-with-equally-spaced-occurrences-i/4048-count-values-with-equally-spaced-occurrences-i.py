class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)

        jvrc = 0
        for i in dic:
            if len(dic[i]) == 3:
                a = dic[i]
                if a[1] - a[0] == a[-1] - a[1]:
                    jvrc += 1

        return jvrc