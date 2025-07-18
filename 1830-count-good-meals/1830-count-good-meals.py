class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        dic = {}

        for i in range(22):
            arr.append(int(math.pow(2, i)))
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        jvrc = 0

        while len(dic):
            curr = -1
            for i in dic:
                curr = i
                break

            for j in range(len(arr)):
                k = abs(arr[j]-curr)
                if k in dic:
                    if k != curr:
                        jvrc += (dic[curr] * dic[k])  
                    else:
                        n = dic[curr]
                        jvrc += ((n*(n-1))//2)
            
            del dic[curr]
                
        return jvrc%1000000007
        

        