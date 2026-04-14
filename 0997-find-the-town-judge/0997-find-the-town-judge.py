class Solution:
    def findJudge(self, n: int, arr: List[List[int]]) -> int:
        dic = {}
        vis = set()

        for i in range(len(arr)):
            if arr[i][1] not in dic:
                dic[arr[i][1]] = 1
            else:
                dic[arr[i][1]] += 1

            vis.add(arr[i][0])

        for i in dic:
            if dic[i] == n-1 and i not in vis:
                return i

        if n==1:
            return n 

        return -1
        