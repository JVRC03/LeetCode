class Solution:
    def numberOfBeams(self, arr: List[str]) -> int:
        curr, jvrc = -1, 0

        for i in range(len(arr)):
            c = arr[i].count('1')
            if curr == -1:
                if c:
                    curr = c
            else:
                if c:
                    jvrc += (c * curr)
                    curr = c

        return jvrc
        