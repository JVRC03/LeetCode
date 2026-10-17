class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        jvrc = 0
        heap = []
        heapq.heapify(heap)
        dic = {}

        for i in range(len(nums)):
            dic[nums[i]] = i
            s, curr = str(nums[i]), 0

            for j in range(len(s)):
                curr += int(s[j])

            heapq.heappush(heap, [curr, nums[i]])
        
        i = 0
        while len(heap):
            arr = heapq.heappop(heap)

            if nums[i] == arr[-1]:
                i += 1
                continue
            
            curr_nums = nums[i]
            curr_idx = i
            nums[i] = arr[-1]
            dic[curr_nums] = dic[arr[-1]]

            nums[dic[arr[-1]]] = curr_nums
            dic[arr[-1]] = i
            
            jvrc += 1
            i += 1
        
        return jvrc


        