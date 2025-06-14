class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
        
        temp = [1] * ( (math.ceil((math.sqrt(sum(nums)))))+100  )

        for i in range(2, int(math.sqrt(len(temp)))+1):
            for j in range(i*i, len(temp), i):
                temp[j] = 0
        
        jvrc = 0

        for i in range(2, len(temp)):
            if temp[i]:
                if p%i == 0:
                    jvrc += 1
        
        return jvrc

        

        