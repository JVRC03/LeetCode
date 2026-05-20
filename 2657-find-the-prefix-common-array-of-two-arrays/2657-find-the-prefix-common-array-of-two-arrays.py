class Solution:
    def findThePrefixCommonArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}

        jvrc = []
        curr = 0

        for i in range(len(arr1)):
            if arr1[i] not in dic:
                dic[arr1[i]] = 1
            else:
                dic[arr1[i]] += 1
            
            if arr2[i] not in dic:
                dic[arr2[i]] = 1
            else:
                dic[arr2[i]] += 1
            
            if dic[arr1[i]] == 2:
                curr += 1
            
            if dic[arr2[i]] == 2 and arr1[i] != arr2[i]:
                curr += 1            
            
            jvrc.append(curr)

        return jvrc

        