class Solution:
    def rangeBitwiseAnd(self, l: int, right: int) -> int:
        jvrc = ''
        
        def dont_know(j):
            temp = ''
            while j:
                temp += str(j%2)
                j //= 2
            
            temp = temp[::-1]
            return temp
        
        temp = dont_know(l)
        maxi = dont_know(right)
        diff = len(maxi)-len(temp)

        kim = '0' * diff
        temp = kim+temp

        def f(s):
            k = 0
            c = 0

            for i in range(len(s)-1, -1, -1):
                if s[i] == '1':
                    k += int(math.pow(2, c)*1)
                c += 1

            return k
        
        for i in range(len(temp)-1, -1, -1):
            if temp[i] == '0':
                jvrc += '0'
                continue
            success = 0
            arr = list(temp)
            for j in range(i, -1, -1):
                if temp[j] == '0':
                    success = 1
                    arr[j]='1'
                    break
                arr[j]='0'
            
            if success:
                ans = f(''.join(arr))
                if l <= ans <= right:
                    jvrc += '0'
                    g = list(temp)
                    g[i] = '0'
                    temp = ''.join(g)
                else:
                    jvrc += '1'
            else:
                jvrc += '1'
        
        jvrc = jvrc[::-1]
        print(jvrc)
        return f(jvrc)







        