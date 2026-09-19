class Solution:
    def ladderLength(self, s1: str, s2: str, arr: list[str]) -> int:
        q = deque([s1])
        st = set(arr)
        jvrc = 0

        def get(s):
            temp = []

            for i in range(len(s)):
                curr = list(s)
                for j in range(26):
                    curr[i] = chr(97 + j)
                    ans = ''.join(curr)

                    if ans != s and ans in st:
                        st.remove(ans)
                        temp.append(ans)
            
            return temp

        while len(q):
            c = len(q)

            for i in range(c):
                node = q.popleft()

                if node == s2:
                    return jvrc + 1
                
                q.extend(get(node))

            jvrc += 1
        
        return 0
        