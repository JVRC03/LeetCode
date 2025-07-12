class Solution:
    def findMatrix(self, jvrc: List[int]) -> List[List[int]]:
        dic = {}
        maxi, val = 0, 0

        for i in range(len(jvrc)):
            if jvrc[i] not in dic:
                dic[jvrc[i]] = 1
            else:
                dic[jvrc[i]] += 1
            
            if dic[jvrc[i]] > maxi:
                maxi = dic[jvrc[i]]
                val = jvrc[i]

        jvrc = []

        for i in range(maxi):
            jvrc.append([val])

        for i in dic:
            if i == val:
                continue
            
            for j in range(dic[i]):
                jvrc[j].append(i)

        return jvrc



        