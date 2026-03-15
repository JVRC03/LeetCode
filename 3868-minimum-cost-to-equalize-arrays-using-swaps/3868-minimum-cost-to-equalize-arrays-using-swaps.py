class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        dic1, dic2 = {}, {}

        for i in range(len(nums1)):
            if nums1[i] not in dic1:
                dic1[nums1[i]] = 1
            else:
                dic1[nums1[i]] += 1

            if nums2[i] not in dic2:
                dic2[nums2[i]] = 1
            else:
                dic2[nums2[i]] += 1

        for i in dic1:
            tot = (dic1[i])
            if i in dic2:
                tot += (dic2[i])

            if tot%2 == 1:
                return -1

        for i in dic2:
            tot = dic2[i]
            if i in dic1:
                tot += dic1[i]

            if tot%2 == 1:
                return -1
        
        arr = []

        for i in dic1:
            pair = [dic1[i]]

            if i in dic2:
                pair.append(dic2[i])
                del dic2[i]
            else:
                pair.append(0)
            
            mid = (pair[0] + pair[1]) // 2
            arr.append(abs(mid - pair[0]))
        
        for i in dic2:
            arr.append(dic2[i]//2)
        
        arr.sort()
        jvrc = 0

        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            
            for j in range(i+1, len(arr)):
                if arr[j] == 0:
                    continue
                if arr[i] < arr[j]:
                    arr[i] -= arr[j]
                    jvrc += arr[j]
                    arr[j] = 0
                else:
                    arr[j] -= arr[i]
                    jvrc += arr[i]
                    arr[i] = 0
                    break
            if arr[i]:
                jvrc += (arr[i]//2)
                break
        return jvrc
        
            
