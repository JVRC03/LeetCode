class Solution:
    def countCompleteDayPairs(self, arr: List[int]) -> int:
        dic = {}

        for i in range(len(arr)):
            v = arr[i]%24

            if v not in dic:
                dic[v] = 1
            else:
                dic[v] += 1
        
        jvrc = 0

        for i in range(len(arr)):
            k = 24-(arr[i]%24)
            if k == 24:
                k = 0
            c = arr[i]%24

            if k in dic:
                if k == 0 or k == c:
                    jvrc += (dic[k]-1)
                else:
                    jvrc += (dic[k])
            
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    del dic[c]
        
        return jvrc
        