class Solution:
    def removeCoveredIntervals(self, arr: List[List[int]]) -> int:
        arr.sort()

        dic ={}
        for i in range(len(arr)):
            if arr[i][0] not in dic:
                dic[arr[i][0]] = [arr[i][1]]
            else:
                dic[arr[i][0]].append(arr[i][1])
        
        for i in range(len(arr)):
            arr[i][1] = dic[arr[i][0]].pop()

        r = 1
        jvrc = [arr[0]]

        while r < len(arr):
            if jvrc[-1][0] <= arr[r][0] and arr[r][1] <= jvrc[-1][-1]:
                r += 1
                continue

            jvrc.append(arr[r])
            r += 1

        return len(jvrc) 



        