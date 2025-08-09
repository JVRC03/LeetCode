class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        dic = {}
        for i in range(len(nums2)):
            nums2[i] *= k
            if nums2[i] not in dic:
                dic[nums2[i]] = 1
            else:
                dic[nums2[i]] += 1
        
        jvrc = 0
        x = max(nums1)
        arr = []
        for i in range(x+1):
            arr.append([-1])
        
        for i in range(1, x+1):
            c = i
            for j in range(i, x+1, c):
                arr[j].append(i)
        
        for i in range(len(nums1)):
            temp = arr[nums1[i]]
            for j in range(1, len(temp)):
                if temp[j] in dic:
                    jvrc += dic[temp[j]]
        
        return jvrc


        

        