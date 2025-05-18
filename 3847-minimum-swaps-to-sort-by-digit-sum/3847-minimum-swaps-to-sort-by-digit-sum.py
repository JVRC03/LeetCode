class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []
        heapq.heapify(arr)
        dic = {}
        idx = {}

        for i in range(len(nums)):
            s = str(nums[i])
            idx[nums[i]] = i
            c = 0
            for j in range(len(s)):
                c += int(s[j])
            print(c)
            if c not in dic:
                dic[c] = []
                heapq.heappush(dic[c], nums[i])
                heapq.heappush(arr, c)
            else:
                heapq.heappush(dic[c], nums[i])
        
        jvrc = 0
        i = 0

        while len(arr):
            a = heapq.heappop(arr)
            temp = dic[a]
            while len(temp):
                k = heapq.heappop(temp)
                if nums[i] == k:
                    i += 1
                    continue
                jvrc += 1
                x = idx[k]
                idx[nums[i]] = x
                nums[x], nums[i] = nums[i], nums[x]
                i += 1

        return jvrc
                



            
        


        