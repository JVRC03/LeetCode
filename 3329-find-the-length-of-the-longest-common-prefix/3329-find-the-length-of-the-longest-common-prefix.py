class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s, jvrc = set(), 0

        for i in range(len(arr1)):
            k = str(arr1[i])
            temp = ''
            for j in range(len(k)):
                temp += k[j]
                s.add(temp)
        
        for i in range(len(arr2)):
            k = str(arr2[i])
            temp = ''
            for j in range(len(k)):
                temp += k[j]
                if temp in s:
                    jvrc = max(jvrc, len(temp))
        
        return jvrc

        