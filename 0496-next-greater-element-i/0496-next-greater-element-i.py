class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = [-1]
        stack = [ [nums2[-1], len(nums2) - 1] ]
        dic = {nums2[-1]: len(nums2) - 1}

        for i in range(len(nums2)-2, -1, -1):
            while len(stack) and stack[-1][0] <= nums2[i]:
                stack.pop()
            
            if not len(stack):
                idx.append(-1)
            else:
                idx.append(stack[-1][0])
            
            stack.append([nums2[i], i])
            dic[nums2[i]] = i
        
        idx = idx[::-1]
        jvrc = []

        for i in range(len(nums1)):
            index = dic[nums1[i]]
            jvrc.append(idx[index])
        
        return jvrc
        