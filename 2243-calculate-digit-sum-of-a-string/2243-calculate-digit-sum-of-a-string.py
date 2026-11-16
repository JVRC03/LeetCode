class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            c, curr = 0, ''
            cnt = 0

            for i in range(len(s)):
                cnt += 1
                c += int(s[i])

                if cnt == k:
                    cnt = 0
                    curr += str(c)
                    c = 0
                
            if cnt:
                curr += str(c)
        
            s = curr
        
        return s





        