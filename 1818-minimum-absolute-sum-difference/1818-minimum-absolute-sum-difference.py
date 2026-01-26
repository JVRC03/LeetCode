class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = nums1.copy()
        arr.sort()
        temp = []

        def check(k):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] < k:
                    f = mid+1
                else:
                    r = mid-1
                    ans = mid
            
            a = float('inf')
            aa = -1
            if ans == -1:
                a = abs(k - arr[-1])
                aa = arr[-1]
            else:
                a = abs(k-arr[ans])
                aa = arr[ans]

            b, c = float('inf'), float('inf')
            bb, cc = float('inf'), float('inf')

            if ans+1 < len(arr):
                b = abs(k-arr[ans+1])
                bb = arr[ans+1]
            
            if ans-1 > -1:
                c = abs(k - arr[ans-1])
                cc = arr[ans-1]
            
            t = [[a, aa], [b, bb], [c, cc]]
            t.sort()

            return t[0][0], t[0][-1]

        for i in range(len(nums1)):
            actual_diff = abs(nums1[i] - nums2[i])
            reduced_diff, ele = check(nums2[i])

            if reduced_diff < actual_diff:
                temp.append([reduced_diff, i, actual_diff-reduced_diff, ele])
        
        idx, curr = -1, 0
        ele = -1

        for i in range(len(temp)):
            if temp[i][2] > curr:
                curr = temp[i][2]
                idx = temp[i][1]
                ele = temp[i][-1]
        
        if ele != -1:
            nums1[idx] = ele
        jvrc = 0

        for i in range(len(nums1)):
            jvrc += abs(nums1[i] - nums2[i])
        
        return jvrc%1000000007

        

        