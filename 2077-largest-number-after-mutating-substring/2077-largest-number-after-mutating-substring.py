class Solution:
    def maximumNumber(self, num: str, arr: List[int]) -> str:
        s = list(num)
        c = -1

        for i in range(len(s)):
            if int(s[i]) < arr[int(s[i])]:
                c = i
                break
        if c == -1:
            return num
        
        for i in range(c, len(s)):
            if arr[int(s[i])] >= int(s[i]):
                s[i] = str(arr[int(s[i])])
                continue
            break

        jvrc = ''.join(s)

        return jvrc

        