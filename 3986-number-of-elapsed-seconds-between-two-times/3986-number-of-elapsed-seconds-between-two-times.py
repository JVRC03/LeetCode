class Solution:
    def secondsBetweenTimes(self, a: str, b: str) -> int:
        h1 = int(str(a[0] + a[1])) * 60 * 60 
        h2 = int(str(b[0] + b[1])) * 60 * 60 

        m1 = int(str(a[3] + a[4])) * 60
        m2 = int(str(b[3] + b[4])) * 60

        s1 = int(str(a[6] + a[7]))
        s2 = int(str(b[6] + b[7]))

        jvrc = (h2 - h1) + (m2 - m1) + (s2 - s1)

        return jvrc

        