class Solution:
    def numberOfWeakCharacters(self, arr: List[List[int]]) -> int:
        arr.sort()
        jvrc = 0
        temp = []

        def fa(fi, k):
            f, r = fi, len(arr)-1
            ans = -1

            while f <= r:
                mid = (f+r)//2

                if arr[mid][0] <= k:
                    f = mid+1
                else:
                    r = mid-1
                    ans = mid
                    
            return ans
        
        curr = arr[-1][-1]

        for i in range(len(arr)-1, -1, -1):
            if arr[i][-1] > curr:
                curr = arr[i][-1]
            temp.append(curr)
        temp = temp[::-1]

        for i in range(len(arr)):
            k = fa(i+1, arr[i][0])
            if k != -1:
                if temp[k] > arr[i][-1]:
                    jvrc += 1

        return jvrc



        