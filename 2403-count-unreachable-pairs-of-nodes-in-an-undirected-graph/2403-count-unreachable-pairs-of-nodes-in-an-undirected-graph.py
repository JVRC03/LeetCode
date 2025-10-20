class Solution:
    def __init__(self):
        self.count = 0

    def countPairs(self, n: int, arr: List[List[int]]) -> int:
        dic = {}
        nums = []

        for i in range(len(arr)):
            k = arr[i]

            if k[0] not in dic:
                dic[k[0]] = [k[1]]
            else:
                dic[k[0]].append(k[1])
            
            if k[1] not in dic:
                dic[k[1]] = [k[0]]
            else:
                dic[k[1]].append(k[0])
        
        for i in range(n):
            if i not in dic:
                dic[i] = []
        v = [0] * n

        def dfs(source):
            if v[source]:
                return
            v[source] = 1
            self.count += 1

            curr = dic[source]

            for i in range(len(curr)):
                dfs(curr[i])

        for i in range(len(v)):
            if v[i] == 0:
                self.count = 0
                dfs(i)
                nums.append(self.count)
        
        p_sum = [nums[0]]
        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1]+nums[i])
        
        jvrc = 0

        for i in range(len(nums)-1):
            k = p_sum[-1]-p_sum[i]
            jvrc += (k * nums[i])
        
        return jvrc
                
        