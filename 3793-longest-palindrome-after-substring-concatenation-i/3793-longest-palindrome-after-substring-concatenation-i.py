class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        jvrc = 0
        arr = []

        def pali(x):
            for i in range(len(x)//2):
                if x[i] != x[len(x)-i-1]:
                    return False
            return True

        
        for i in range(len(t)):
            temp = ''
            for j in range(i, len(t)):
                temp += t[j]
                if pali(temp):
                    jvrc = max(jvrc, len(temp))
                arr.append(temp)

        for i in range(len(s)):
            temp = ''
            for j in range(i, len(s)):
                temp += s[j]
                if pali(temp):
                    jvrc = max(jvrc, len(temp))
                for k in range(len(arr)):
                    if pali(temp+arr[k]):
                        jvrc = max(jvrc, len(temp)+len(arr[k]))


        return jvrc

        