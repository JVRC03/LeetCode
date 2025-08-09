class Solution:
    def numTeams(self, arr: List[int]) -> int:

        def f(nums):
            temp = []

            for i in range(len(nums)):
                c = 0
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        c += 1
                
                temp.append([nums[i], c])
            
            jvrc = 0

            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        jvrc += temp[j][-1]
            
            return jvrc
        
        return f(arr)+f(arr[::-1])
        