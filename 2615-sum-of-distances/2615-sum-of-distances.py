class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        
        jvrc = [-1] * len(nums)

        for idx in dic:
            p_sum = []
            arr = dic[idx]

            if len(arr) == 1:
                jvrc[arr[-1]] = 0
                continue

            for i in range(len(arr)):
                if not len(p_sum):
                    p_sum.append(arr[i])
                else:
                    p_sum.append(arr[i] + p_sum[-1])

            for i in range(len(arr)):
                
                left = i * arr[i]
                right = (len(arr) - i - 1) * arr[i]

                if i == len(arr) - 1:
                    jvrc[arr[i]] = abs(left - p_sum[-2])
                    continue

                if i > 0:
                    left = abs(left - p_sum[i-1])
                right = abs(right- (p_sum[-1] - p_sum[i]))

                jvrc[arr[i]] = (left + right)
        
        return jvrc
                
                




            
        