class Solution:
    def maximumEnergy(self, arr: List[int], k: int) -> int:
        dic = {}
        jvrc = float('-inf')

        for i in range(len(arr)-1, -1, -1):
            e = i%k

            if e not in dic:
                dic[e] = arr[i]
            else:
                dic[e] += arr[i]
            
            jvrc = max(jvrc, dic[e])
        

        return jvrc


        