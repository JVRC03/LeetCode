class Solution:
    def partitionString(self, s: str) -> List[str]:
        cur = ''
        st = set()
        jvrc = []
        r = 0

        while r < len(s):
            cur += s[r]

            if cur not in st:
                st.add(cur)
                jvrc.append(cur)
                cur = ''
            r += 1

        if cur not in st and len(cur) > 0:
            jvrc.append(cur)

        return jvrc
        