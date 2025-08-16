class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
       
        def f(a, b):
            s = set()
            jvrc = 0

            for i in range(len(b)):
                temp = '*'
                for j in range(i, len(b)):
                    temp += str(b[j])
                    temp += '*'
                    s.add(temp)

            for i in range(len(a)):
                temp = '*'
                for j in range(i, len(a)):
                    temp += str(a[j])
                    temp += '*'
                    if temp in s:
                        jvrc = max(jvrc, (j-i)+1)
            
            return jvrc
            
        if len(nums1) < len(nums2):
            return f(nums2, nums1)
        
        return f(nums1, nums2)
        




        