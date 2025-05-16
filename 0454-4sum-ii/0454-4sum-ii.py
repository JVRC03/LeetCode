class Solution:
    def fourSumCount(self, n1: List[int], n2: List[int], n3: List[int], n4: List[int]) -> int:
        dic = {}

        for i in range(len(n3)):
            for j in range(len(n4)):
                k = n3[i]+n4[j]
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

        jvrc = 0
        for i in range(len(n1)):
            for j in range(len(n2)):
                temp = n1[i]+n2[j]
                if -temp in dic:
                    jvrc += dic[-temp]
                
        return jvrc                           





        return jvrc
        