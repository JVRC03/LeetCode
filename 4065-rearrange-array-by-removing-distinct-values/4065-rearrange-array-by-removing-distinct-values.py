class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        jvrc, status = [], True

        while status:
            curr = []
            anys = 0
            for i in dic:
                if dic[i]:
                    anys = 1
                    curr.append(i)
                    dic[i] -= 1

            status = anys

            curr.sort()
            jvrc.extend(curr)
        
        return jvrc
        