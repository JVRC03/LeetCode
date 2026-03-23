class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        f, r = 1, len(nums)
        jvrc = float('-inf')

        def check(idx, nums, k):
            maxi = -1
            dic = {}
            heap = []
            heapq.heapify(heap)

            for i in range(idx):
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1
            
            for i in dic:
                temp = [-dic[i], i]
                heapq.heappush(heap, temp)
            
            maxi = -heap[0][0]
            rem = idx - maxi
            if rem <= k:
                return True, maxi
            
            f = 0
            for i in range(idx, len(nums)):
                dic[nums[f]] -= 1    
                temp = [-dic[nums[f]], nums[f]]
                f += 1
                heapq.heappush(heap, temp)
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1
                temp = [-dic[nums[i]], nums[i]]
                heapq.heappush(heap, temp)

                local = -1

                while True:
                    temp = heapq.heappop(heap)
                    if abs(temp[0]) == dic[temp[1]]:
                        local = abs(temp[0])
                        heapq.heappush(heap, temp)
                        break
                
                rem = idx - local
                if rem <= k:
                    return True, local
            
            return False, -1

        while f <= r:
            mid = f + ((r - f) // 2)
            status, ans = check(mid, nums, k)

            if status:
                jvrc = max(jvrc, ans)
                f = mid + 1
            else:
                r = mid - 1
        
        return jvrc
        