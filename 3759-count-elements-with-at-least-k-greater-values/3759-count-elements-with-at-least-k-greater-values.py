class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        dic = {}
        curr, jvrc = nums[-1], 0
        tot = 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
            
            if curr == nums[i]:
                if tot >= k:
                    jvrc += 1
            else:
                tot += dic[curr]
                curr = nums[i]

                if tot >= k:
                    jvrc += 1

        return jvrc
        
        