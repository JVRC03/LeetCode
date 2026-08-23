class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        maxi = max(nums)
        prime = [1] * (maxi + 1)
        prime[0] = 0
        prime[1] = 0
        dic = {}

        for i in range(maxi + 1):
            if prime[i]:
                #dic[i] = [i]
                c = i
                for j in range(c, len(prime), c):
                    prime[j] = 0
                    
                    if j not in dic:
                        dic[j] = [i]
                    else:
                        dic[j].append(i)
        
        d = {}
        f, r = 0, 0
        jvrc = 0
        while f <= r and r < len(nums):
            arr = dic[nums[r]]
            for i in range(len(arr)):
                if arr[i] not in d:
                    d[arr[i]] = 1
                else:
                    d[arr[i]] += 1
            
            if len(d) <= k:
                jvrc = max(jvrc, (r - f) + 1)
                r += 1
                continue
            
            while len(d) > k:
                arr = dic[nums[f]]
                for i in range(len(arr)):
                    d[arr[i]] -= 1
                    if not d[arr[i]]:
                        del d[arr[i]]
                f += 1
                
            r += 1

        return jvrc
            

        