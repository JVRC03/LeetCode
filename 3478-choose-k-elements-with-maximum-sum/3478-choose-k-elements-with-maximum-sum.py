class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        if len(nums1) < 2:
            return [0]
        
        temp, dic = {}, {}
        jvrc = []

        for i in range(len(nums1)):
            if nums1[i] not in temp:
                temp[nums1[i]] = [nums2[i]]
            else:
                temp[nums1[i]].append(nums2[i])
            
        arr, heap = list(temp.keys()), []
        heapq.heapify(heap)

        arr.sort()
        curr = 0

        for i in range(len(arr)):
            dic[arr[i]] = curr

            x = temp[arr[i]]

            for j in range(len(x)):
                
                if len(heap) < k:
                    heapq.heappush(heap, x[j])
                    curr += x[j]
                else:
                    heapq.heappush(heap, x[j])
                    curr+= x[j]
                    curr -= heapq.heappop(heap)
            
        
        for i in range(len(nums1)):
            jvrc.append(dic[nums1[i]])
        
        return jvrc

                






        


