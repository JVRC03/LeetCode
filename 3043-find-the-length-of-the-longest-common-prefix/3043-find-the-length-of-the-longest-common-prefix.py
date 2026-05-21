class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        jvrc, s = 0, set()

        for i in range(len(arr2)):
            temp = ''
            sa = str(arr2[i])
            for j in range(len(sa)):
                temp += sa[j]
                s.add(temp)
        
        for i in range(len(arr1)):
            temp = ''
            sa = str(arr1[i])

            for j in range(len(sa)):
                temp += sa[j]

                if temp in s:
                    jvrc = max(jvrc, len(temp))
        
        return jvrc
        