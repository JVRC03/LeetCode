class Solution:
    def minimumRemoval(self, arr: List[int]) -> int:
        arr.sort()
        if len(arr) == 1:
            return 0
        
        p_sum = [arr[0]]
        dic = {arr[0] : 0}



        for i in range(1, len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = i
            p_sum.append(arr[i] + p_sum[-1])

        def check():
            jvrc = float('inf')
            a, b = 0, 0

            for i in range(1, len(arr)-1):

                idx = dic[arr[i]]
                k = 0
                if idx != 0:
                    k = p_sum[idx-1]
                
                k += abs((arr[i] * (len(arr)-i-1))- (p_sum[-1]-p_sum[i]))
                
                jvrc = min(jvrc, k)
                a += (abs(arr[0]-arr[i]))
                if arr[-1] > arr[i]:
                    b += arr[i]
                
            if arr[0] < arr[-1]:
                b += arr[0]
            a += (abs(arr[0]-arr[-1]))

            return min(jvrc, a, b)

        return check()
        