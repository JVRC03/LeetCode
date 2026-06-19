class Solution:
    def largestAltitude(self, arr: List[int]) -> int:
        jvrc = 0
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]

            jvrc = max(jvrc, curr)
        
        return jvrc

        