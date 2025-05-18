class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        nums = arr.copy()
        nums.sort()
        jvrc = []
        
        while len(nums):
            a = nums.pop()
            temp = []

            for i in range(len(arr)):
                temp.append(arr[i])

                if arr[i] == a:
                    break
                
            jvrc.append(len(temp))
            jvrc.append(len(nums)+1)
            for i in range(len(temp)):
                arr[i] = temp[-i-1]
            
            temp = []

            for i in range(len(nums)+1):
                temp.append(arr[i])
            for i in range(len(temp)):
                arr[i] = temp[-i-1]

        return jvrc
        