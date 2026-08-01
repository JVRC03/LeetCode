class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        def mini(a, b):
            if len(a) > 6 * len(b):
                return True
            
            return 0

        if mini(nums1, nums2) or mini(nums2, nums1):
            return -1 
        
        dic1, dic2 = {}, {}
        a, b = 0, 0

        for i in range(len(nums1)):
            if nums1[i] not in dic1:
                dic1[nums1[i]] = 1
            else:
                dic1[nums1[i]] += 1
            a += nums1[i]
        
        for i in range(len(nums2)):
            if nums2[i] not in dic2:
                dic2[nums2[i]] = 1
            else:
                dic2[nums2[i]] += 1
            b += nums2[i]
        
        def get(x, y, A, B):
            jvrc = 0

            while x > y:
                jvrc += 1
                a = max(A.keys())
                b = min(B.keys())

                diff_a = a - 1
                diff_b = 6 - b

                if diff_a > diff_b:
                    if 1 not in A:
                        A[1] = 0
                    A[1] += 1
                    x -= (a - 1)
                    A[a] -= 1
                    if not A[a]:
                        del A[a]
                else:
                    if 6 not in B:
                        B[6] = 0
                    B[6] += 1
                    y += 6
                    y -= b

                    B[b] -= 1
                    if not B[b]:
                        del B[b]

            
            return jvrc

        if a > b:
            return get(a, b, dic1, dic2)
        
        return get(b, a, dic2, dic1)
        


        