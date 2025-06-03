class Solution:
    
    def check(self, dic, k):
        for i in dic:
            if dic[i] < k:
                return False
        return True

    def f(self, s, dic, k):
        f, r = 0, 0
        ans = 0
        temp = {}

        while f <= r and r < len(s):
            if dic[s[r]] < k:
                if self.check(temp, k):
                    ans = max(ans, (r-f))
                while f <= r:
                    dic[s[f]] -= 1
                    f += 1
                r += 1
                temp = {}
                continue
            if s[r] not in temp:
                temp[s[r]] = 1
            else:
                temp[s[r]] += 1

            r += 1
        
        ans = max(ans, (r-f))

        return ans

    def longestSubstring(self, s: str, k: int) -> int:
        dic = {}
        jvrc = 0
        st = set()

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for i in dic:
            if dic[i] < k:
                st.add(i)

        r = 0

        while r < len(s):
            if s[r] in st:
                r += 1
                continue
            idx = -1
            temp = {}
            n = ''
            for i in range(r, len(s)):
                if s[i] in st:
                    idx = i
                    break
                if s[i] not in temp:
                    temp[s[i]] = 1
                else:
                    temp[s[i]] += 1
                n += s[i]
            
            r = idx

            jvrc = max(jvrc, self.f(n, temp, k))

            if r == -1:
                break
        
        return jvrc            

            

 

        