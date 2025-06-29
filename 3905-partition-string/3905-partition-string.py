class Solution:
    def partitionString(self, s: str) -> List[str]:
        curr = ''
        st = set()
        jvrc = []
        r = 0

        while r < len(s):
            curr += s[r]

            if curr not in st:
                st.add(curr)
                jvrc.append(curr)
                curr = ''
            r += 1

        if curr not in st and len(curr) > 0:
            jvrc.append(curr)

        return jvrc
        