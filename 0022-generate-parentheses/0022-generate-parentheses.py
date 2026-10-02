class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.jvrc = []

        def check(s):
            stack = 0
            for i in range(len(s)):
                if s[i] == '(':
                    stack += 1
                else:
                    if stack:
                        stack -= 1
                    else:
                        return False
            
            if stack:
                return False
            return True

        def func(n, s):

            if n == 0:
                if check(s):
                    self.jvrc.append(s)
                return

            func(n - 1, s + '(')
            func(n - 1, s + ')')

        func(n * 2, '')
        return self.jvrc
        