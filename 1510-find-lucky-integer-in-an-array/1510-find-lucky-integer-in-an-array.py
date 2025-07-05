class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}

        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        jvrc = -1

        for i in dic:
            if dic[i] == i:
                jvrc = max(jvrc, i)
        
        return jvrc
        