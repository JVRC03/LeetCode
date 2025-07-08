class Solution:
    def maximumPopulation(self, arr: List[List[int]]) -> int:
        dic = {}

        for i in range(len(arr)):
            for j in range(arr[i][0], arr[i][1]):
                if j not in dic:
                    dic[j] = 1
                else:
                    dic[j] += 1
        
        jvrc = -1
        curr = 0

        for i in dic:
            if dic[i] > curr:
                curr = dic[i]
                jvrc = i
            elif dic[i] == curr:
                jvrc = min(jvrc, i)
        
        return jvrc
        