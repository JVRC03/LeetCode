class Solution:
    def averageWaitingTime(self, arr: List[List[int]]) -> float:
        curr = arr[0][0]+arr[0][1]
        jvrc = arr[0][-1]

        for i in range(1, len(arr)):
            k = curr-arr[i][0]
            
            if k > 0:
                jvrc += k
            jvrc += arr[i][-1]

            curr += arr[i][-1]
            if k < 0:
                curr += abs(k)
        
        return jvrc/len(arr)

        