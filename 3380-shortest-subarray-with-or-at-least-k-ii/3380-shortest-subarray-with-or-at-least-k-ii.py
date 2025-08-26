class Solution:
    def check(self, dic, k):
        m = max(dic.keys())
        c = 0
        a = 0

        while c <= m:
            if c in dic and dic[c] > 0:
                a += int(math.pow(2, c))
            c += 1

        if a >= k:
            return True, 0
        
        return False, a

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = {}
        curr, jvrc = 0, float('inf')

        f, r = 0, 0

        while f <= r and r < len(nums):
            curr |= nums[r]
            s = bin(nums[r])
            s = s[2:]
            c = 0

            for i in range(len(s)-1, -1, -1):
                if s[i] == '1':
                    if c not in dic:
                        dic[c] = 1
                    else:
                        dic[c] += 1
                c += 1

            if curr >= k:

                while curr >= k and f <= r:
                    jvrc = min(jvrc, (r-f)+1)
                    s = bin(nums[f])
                    s = s[2:]
                    c = 0

                    for i in range(len(s)-1, -1, -1):
                        if s[i] == '1':
                            dic[c] -= 1
                            
                        c += 1
                    
                    x, y = self.check(dic, k)

                    if x == False:
                        curr = y

                    f += 1
            
            r += 1
        
        if jvrc == float('inf'):
            jvrc = -1

        return jvrc

        