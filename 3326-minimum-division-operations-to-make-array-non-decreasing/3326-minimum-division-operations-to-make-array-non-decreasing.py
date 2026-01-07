class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        dic = {}

        def f(n):
            if n in dic:
                return dic[n]
                
            for i in range(2, int(math.sqrt(n))+1):
                if n%i == 0:
                    dic[n] = i
                    return i
            
            return n
                
        jvrc, curr = 0, nums[-1]

        for i in range(len(nums)-2, -1, -1):

            if curr >= nums[i]:
                curr = nums[i]
                continue
            
            c = f(nums[i])
            if curr >= c:
                curr = c
                jvrc += 1
                continue
            
            return -1
        
        return jvrc
        