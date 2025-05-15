class Solution:
    def minimumCardPickup(self, arr: List[int]) -> int:
        dic = {}
        jvrc = float('inf')

        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = i
            else:
                jvrc = min(jvrc, i+1-dic[arr[i]])
                dic[arr[i]] = i
        
        if jvrc == float('inf'):
            return -1
        
        return jvrc
        