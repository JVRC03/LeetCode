class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        jvrc = [-1] * len(nums)
        temp, f = [], 0
        c = 0

        for i in range(len(nums)):
            if nums[i] < pivot:
                jvrc[f] = nums[i]
                f += 1
            elif nums[i] == pivot:
                c += 1
            else:
                temp.append(nums[i])
        
        for i in range(c):
            jvrc[f] = pivot
            f += 1
            
        for i in range(len(temp)):
            jvrc[f] = temp[i]
            f += 1
        
        return jvrc
        