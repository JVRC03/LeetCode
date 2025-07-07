class Solution:
    def concatHex36(self, n: int) -> str:

        def f(x, idx):
            s = ''

            while x >= idx:
                r = str(x%idx)
                if int(r) < 10:
                    s += r
                else:
                    s += chr(55+int(r))

                x //= idx

            if x:
                if 10 <= x:
                    s += chr(55+x)
                else:
                    s += str(x)
                 
            return s[::-1]

        jv, rc = f(n*n, 16), f((n*n*n), 36)

        return jv+rc 