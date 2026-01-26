class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        jvrc=[]
        curr = float('inf')

        for i in range(len(arr)-1):
            k = arr[i+1] - arr[i]

            if k < curr:
                jvrc = []
                jvrc.append([arr[i], arr[i+1]])
                curr = k
            elif k == curr:
                jvrc.append([arr[i], arr[i+1]])
        
        return jvrc
        