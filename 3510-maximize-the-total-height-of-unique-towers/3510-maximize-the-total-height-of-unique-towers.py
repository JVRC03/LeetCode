class Solution:
    def maximumTotalSum(self, arr: List[int]) -> int:
        arr.sort()
        curr = float('inf')
        s = set()
        jvrc = 0

        while len(arr):
            curr = min(curr, arr[-1])

            if curr not in s:
                s.add(curr)
                jvrc += curr
                arr.pop()
                continue
            if curr-1 == 0:
                return -1
            
            s.add(curr-1)
            curr = (curr-1)
            arr.pop()
            jvrc += (curr)
        
        return jvrc

        