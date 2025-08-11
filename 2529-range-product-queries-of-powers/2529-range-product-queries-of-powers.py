class Solution:
    def productQueries(self, n: int, q: List[List[int]]) -> List[int]:
        a = bin(n)
        a = a[2:]
        c = 0
        arr = []

        for i in range(len(a)-1, -1, -1):
            if a[i] == '1':
                k = int(math.pow(2, c))
                arr.append(k)
            c += 1

        for i in range(1, len(arr)):
            arr[i] *= arr[i-1]
        
        jvrc = []
        for i in range(len(q)):
            if q[i][0] == 0:
                jvrc.append(arr[q[i][1]]%1000000007)
                continue
            
            jvrc.append( (arr[q[i][1]]//arr[q[i][0]-1]) % 1000000007 )
        
        return jvrc
        



        