class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        def f(k):
            n = int(math.sqrt(k))+1

            if k <= 1:
                return False
                
            for i in range(2, n):
                if k%i == 0:
                    return False
            return True

        for i in dic:
            if f(dic[i]):
                return True

        return False
        