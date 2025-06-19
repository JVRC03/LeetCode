class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:

        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(dic[nums[i]][-1]+i)
        
        temp = {} 

        jvrc = []

        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 1
            else:
                temp[nums[i]] += 1

            arr = dic[nums[i]]

            k = -1
            
            if temp[nums[i]] == 1:
                r = (len(arr)-1) * (i)
                k = abs(arr[-1]-arr[0]-r)
            elif temp[nums[i]] == len(arr):
                l = (len(arr)) * i
                k = abs(arr[-1]-l)
            else:
                l = (temp[nums[i]]-1) * i
                r = (len(arr)-temp[nums[i]]) * i

                k = abs( arr[temp[nums[i]]-2] - l) + abs((arr[-1]-arr[temp[nums[i]]-1])- r)

            jvrc.append(k)
        
        return jvrc
        