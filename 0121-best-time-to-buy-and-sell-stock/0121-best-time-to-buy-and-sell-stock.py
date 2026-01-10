class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        temp = [0] * len(arr)
        temp[-1] = 0

        curr = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            if curr <= arr[i]:
                temp[i] = 0
            else:
                temp[i] = curr
            
            curr = max(curr, arr[i])
        
        jvrc = 0
        print(temp)

        for i in range(len(arr)):
            if temp[i]:
                jvrc = max(jvrc, abs(temp[i] - arr[i]))
        
        return jvrc
        