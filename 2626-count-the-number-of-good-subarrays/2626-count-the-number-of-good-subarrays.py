class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        f, r = 0, 0
        jvrc, c = 0, 0
        dic = {}

        while f <= r and r < len(nums):
            if nums[r] not in dic:
                dic[nums[r]] = 1
            else:
                if dic[nums[r]] == 1:
                    dic[nums[r]] += 1
                    c += 1
                else:
                    n = dic[nums[r]]
                    c -= ((n*(n-1))//2)
                    dic[nums[r]] += 1
                    n = dic[nums[r]]
                    c += ((n*(n-1))//2)
            
            if c >= k:
                while c >= k:
                    jvrc += (len(nums)-r)
                    n = dic[nums[f]]
                    c -= ((n*(n-1))//2)
                    dic[nums[f]] -= 1
                    n = dic[nums[f]]
                    c += ((n*(n-1))//2)
                    f += 1
            
            r += 1
        
        while c >= k:
            jvrc += (len(nums)-r)
            n = dic[nums[f]]
            c -= ((n*(n-1))//2)
            dic[nums[f]] -= 1
            n = dic[nums[f]]
            c += ((n*(n-1))//2)
            f += 1
        
        return jvrc

        

            
        