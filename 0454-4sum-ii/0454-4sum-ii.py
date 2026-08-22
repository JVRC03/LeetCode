class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = {}

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                curr = nums3[i] + nums4[j]

                if curr not in dic:
                    dic[curr] = 1
                else:
                    dic[curr] += 1
            
        jvrc = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                curr = nums1[i] + nums2[j]

                diff = -curr

                if diff in dic:
                    jvrc += dic[diff]
        
        return jvrc
        