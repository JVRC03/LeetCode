class Solution:
    def countMajoritySubarrays(self, nums: List[int], k: int) -> int:
        jvrc = 0
        
        for i in range(len(nums)):
            dic = {}
            
            for j in range(i, len(nums)):
                if nums[j] not in dic:
                    dic[nums[j]] = 1
                else:
                    dic[nums[j]] += 1

                if k in dic:
                    if dic[k] > ((j-i)+1)//2:
                        jvrc += 1

        return jvrc
        