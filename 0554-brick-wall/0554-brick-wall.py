class Solution:
    def leastBricks(self, arr: List[List[int]]) -> int:
        dic = {}
        jvrc = 0

        for i in range(len(arr)):
            curr = 0
            for j in range(len(arr[i])):
                curr += arr[i][j]
                if curr not in dic:
                    dic[curr] = 1
                else:
                    dic[curr] += 1
                
                if j != len(arr[i])-1:
                    jvrc = max(jvrc, dic[curr])
        
        return len(arr)-jvrc
        