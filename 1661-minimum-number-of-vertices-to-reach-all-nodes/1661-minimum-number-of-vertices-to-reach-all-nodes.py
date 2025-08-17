class Solution:
    def findSmallestSetOfVertices(self, n: int, arr: List[List[int]]) -> List[int]:
        jvrc = []

        s = set()

        for i in range(len(arr)):
            s.add(arr[i][-1])
       
        for i in range(n):
            if i not in s:
                jvrc.append(i)

        return jvrc

        