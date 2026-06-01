class Solution:
    def minimumCost(self, arr: List[int]) -> int:
        arr.sort()

        jvrc = 0
        while len(arr):
            jvrc += arr.pop()
            if len(arr):
                jvrc += arr.pop()
            
            if len(arr):
                arr.pop()
        
        return jvrc
        