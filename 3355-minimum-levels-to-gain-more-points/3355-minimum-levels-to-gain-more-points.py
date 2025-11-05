class Solution:
    def minimumLevels(self, arr: List[int]) -> int:
        p_sum = []

        if arr[0] == 0:
            p_sum.append(-1)
        else:
            p_sum.append(1)

        for i in range(1, len(arr)):
            if arr[i]:
                p_sum.append(p_sum[-1]+1)
            else:
                p_sum.append(p_sum[-1]-1)
        
        jvrc = float('inf')
        count = float('-inf')

        for i in range(1, len(arr)):
            a = p_sum[i-1]
            b = p_sum[-1]-p_sum[i-1]

            if a > b:
                if count < a:
                    count = a
                    jvrc = min(i, jvrc)
           
        if len(arr) == 2:
            if arr[0] > arr[-1]:
                return 1
            return -1
        
        if jvrc == float('inf'):
            jvrc = -1

        return jvrc

        