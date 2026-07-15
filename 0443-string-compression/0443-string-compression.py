class Solution:
    def compress(self, arr: List[str]) -> int:
        curr, val = arr[0], 0
        jvrc = []

        for i in range(len(arr)):
            if arr[i] == curr:
                val += 1
                continue
            
            jvrc.append(curr)
            if val != 1:
                k = str(val)
                a = list(k)
                jvrc.extend(a)

            curr = arr[i]
            val = 1

        jvrc.append(curr)
        if val != 1:
            k = str(val)
            a = list(k)
            jvrc.extend(a)
        
        for i in range(len(jvrc)):
            arr[i] = jvrc[i]

        while len(arr) > len(jvrc):
            arr.pop()

        return len(jvrc)
        