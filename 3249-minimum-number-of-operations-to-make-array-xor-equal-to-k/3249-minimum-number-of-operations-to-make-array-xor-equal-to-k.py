class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        jvrc = 0

        def f(n):
            cc = 1
            while n:
                if n%2 == 1:
                    if cc in dic:
                        dic[cc] += 1
                    else:
                        dic[cc] = 1
                n //= 2
                cc += 1
        
        for i in range(len(nums)):
            f(nums[i])
        
        s = ''
        while k:
            s += str(k%2)
            k //= 2
        c = 1

        for i in range(len(s)):
            if s[i] == '1':
                if (i+1) in dic:
                    if dic[(i+1)]%2 != 1:
                        jvrc += 1
                else:
                    jvrc += 1
            else:
                if (i+1) in dic:
                    if dic[i+1]%2 == 1:
                        jvrc += 1
            c += 1

        if len(dic) and c <= max(dic.keys()) :
            for i in range(c, max(dic)+1):
                if (i) in dic:
                    if dic[i]%2 == 1:
                        jvrc += 1
        else:
            if len(dic) == 0:
                for i in range(c, len(s)+1):
                    if (i) in dic:
                        if dic[i]%2 == 1:
                            jvrc += 1
                    else:
                        jvrc += 1
            
        return jvrc