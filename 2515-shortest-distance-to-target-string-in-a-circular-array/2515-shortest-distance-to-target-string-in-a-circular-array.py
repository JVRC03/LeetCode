class Solution:
    def closestTarget(self, arr: List[str], k: str, idx: int) -> int:
        temp = []
        jvrc = float('inf')

        for i in range(len(arr)):
            if arr[i] == k:
                temp.append(i)
        
        if not len(temp):
            return -1

        for i in range(len(temp)):
            a = abs(temp[i] - idx)
            jvrc = min(jvrc, a)
        
        if idx < temp[0]:
            jvrc = min(jvrc, idx+(len(arr) - temp[-1]))
        
        if idx > temp[-1]:
            jvrc = min(jvrc, (len(arr) - idx - 1) + temp[0] + 1)

        return jvrc

        