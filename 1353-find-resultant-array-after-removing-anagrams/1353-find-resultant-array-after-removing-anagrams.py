class Solution:
    def removeAnagrams(self, arr: List[str]) -> List[str]:
        a = list(arr[0])
        a.sort()
        curr = ''.join(a)
        jvrc = [arr[0]]

        r = 1

        while r < len(arr):
            temp = list(arr[r])
            temp.sort()
            s = ''.join(temp)

            if s == curr:
                r += 1
                continue
            curr = s
            jvrc.append(arr[r])
            r += 1

        return jvrc
        