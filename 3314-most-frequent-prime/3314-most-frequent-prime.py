class Solution:

    def prime(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        
        return True

    def naadhi(self, mat, i, j):
        arr = []

        a, b = i, j
        s = ''
        while a >= 0:
            s += str(mat[a][b])
            a -= 1
            arr.append(int(s))

        a, b = i, j
        s = ''
        while a < len(mat):
            s += str(mat[a][b])
            a += 1
            arr.append(int(s))    

        a, b = i, j
        s = ''
        while b >= 0:
            s += str(mat[a][b])
            b -= 1
            arr.append(int(s))   

        a, b = i, j
        s = ''
        while b < len(mat[0]):
            s += str(mat[a][b])
            b += 1
            arr.append(int(s))



        a, b = i, j
        s = ''
        while a >= 0 and b >= 0:
            s += str(mat[a][b])
            a -= 1
            b -= 1
            arr.append(int(s))

        a, b = i, j
        s = ''
        while a >= 0 and b < len(mat[0]):
            s += str(mat[a][b])
            a -= 1
            b += 1
            arr.append(int(s))

        a, b = i, j
        s = ''
        while a < len(mat) and b >= 0:
            s += str(mat[a][b])
            a += 1
            b -= 1
            arr.append(int(s))

        a, b = i, j
        s = ''
        while a < len(mat) and b < len(mat[0]):
            s += str(mat[a][b])
            a += 1
            b += 1
            arr.append(int(s))

        return arr

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        jvrc, count = -1, 0    
        dic = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                arr = self.naadhi(mat, i, j)
                for k in range(len(arr)):
                    if arr[k] > 10 and self.prime(arr[k]):
                        if arr[k] not in dic:
                            dic[arr[k]] = 1
                        else:
                            dic[arr[k]] += 1
                        if count < dic[arr[k]]:
                            count = dic[arr[k]]
                            jvrc = arr[k]
                        elif count == dic[arr[k]]:
                            jvrc = max(jvrc, arr[k])

        return jvrc

        