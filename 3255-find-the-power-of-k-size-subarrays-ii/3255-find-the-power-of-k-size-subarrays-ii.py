class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums        

        temp = []

        for i in range(len(nums)):
            temp.append([1, 1])

        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                continue
            
            temp[i-1][-1] = 0
            temp[i][0] = 0

        arr = []
        
        for i in range(len(temp)):
            arr.append(temp[i][0])
            arr.append(temp[i][-1])

        for i in range(1, len(arr)):
            arr[i] = arr[i]+arr[i-1]

        jvrc = []
        f, r = 1, ((k * 2)-2)
        c = k-1

        while r < len(arr):
            tot = arr[r]-arr[f-1]
            
            if tot == r-(f-1):
                jvrc.append(nums[c])
            else:
                jvrc.append(-1)
            
            f += 2
            r += 2
            c += 1

        return jvrc
        