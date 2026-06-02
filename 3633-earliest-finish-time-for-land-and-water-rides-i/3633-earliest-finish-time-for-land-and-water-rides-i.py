class Solution:
    def earliestFinishTime(self, a1: List[int], a2: List[int], b1: List[int], b2: List[int]):
        arr = []
        jvrc = float('inf')

        for i in range(len(a1)):
            arr.append([a1[i], a1[i]+a2[i]])

        for i in range(len(b1)):
            for j in range(len(arr)):
                b = [b1[i], b1[i] + b2[i]]
                a = arr[j]
                if a[0] > b[0]:
                    temp = a
                    a = b
                    b = temp

                c = a[1]

                if b[0] > a[1]:
                    c += abs(a[1]-b[0])
                c += (b[1]-b[0])        

                jvrc = min(jvrc, c)
        
        return jvrc