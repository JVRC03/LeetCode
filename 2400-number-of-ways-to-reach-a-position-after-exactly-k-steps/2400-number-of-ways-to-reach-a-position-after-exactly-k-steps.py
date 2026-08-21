class Solution:
    def numberOfWays(self, a: int, b: int, k: int) -> int:
        dic = {a: {}}
        for i in range(1, k + 1):
            dic[a - i] = {}
            dic[a + i] = {}

        def func(a, b, k):
            if k == 0:
                if a == b:
                    return 1
                return 0
            
            if k in dic[a]:
                return dic[a][k]

            left = func(a - 1, b, k - 1)
            right = func(a + 1, b, k - 1)
          
            dic[a][k] = left + right 
            return dic[a][k]

        return func(a, b, k) % 1000000007
        