class Solution:
    def findChampion(self, n: int, arr: List[List[int]]) -> int:
        s = set()

        for i in range(len(arr)):
            s.add(arr[i][-1])
        
        if len(s) != n-1:
            return -1
        
        for i in range(n):
            if i not in s:
                return i
        

        