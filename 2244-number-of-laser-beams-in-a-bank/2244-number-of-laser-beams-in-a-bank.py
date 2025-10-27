class Solution:
    def numberOfBeams(self, arr: List[str]) -> int:
        temp = []

        for i in range(len(arr)):
            c = arr[i].count('1')
            if c:
                temp.append(c)
        
        jvrc = 0

        for i in range(len(temp)-1):
            jvrc += (temp[i] * temp[i+1])

        return jvrc
        