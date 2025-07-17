class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i]*nums[j]

                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

        jvrc = 0

        for i in dic:
            jvrc += (dic[i]*4*(dic[i]-1))

        return jvrc