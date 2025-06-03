class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        temp = [0] * 101

        for i in range(k):
            n = 50+nums[i]
            temp[n] += 1
        
        n, f = x, 0
        jvrc = []
        ans = -1

        for i in range(101):
            if temp[i] < n:
                n -= temp[i]
            else:
                ans = i-50
                break
        if ans < 0:
            jvrc.append(ans)
        else:
            jvrc.append(0)

        for i in range(k, len(nums)):
            temp[50+nums[f]] -= 1
            temp[50+nums[i]] += 1

            n, ans = x, -1

            for j in range(101):
                if temp[j] < n:
                    n -= temp[j]
                else:
                    ans = j-50
                    break
            if ans < 0:
                jvrc.append(ans)
            else:
                jvrc.append(0)
            f += 1
        
        return jvrc
            


            
    

    

            
        