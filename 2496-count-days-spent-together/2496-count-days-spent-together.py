class Solution:
    def countDaysTogether(self, a: str, al: str, b: str, bl: str) -> int:

        def f(n, d):
            arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            curr = 0

            for i in range(n-1):
                curr += arr[i]
            curr += d

            return curr
        
        d1 = f (( (int(a[0])*10) + int(a[1]) ) , ( (int(a[3])*10) + int(a[4]) ))
        d2 = f (( (int(al[0])*10) + int(al[1]) ) , ( (int(al[3])*10) + int(al[4]) ))
        d3 = f (( (int(b[0])*10) + int(b[1]) ) , ( (int(b[3])*10) + int(b[4]) ))
        d4 = f (( (int(bl[0])*10) + int(bl[1]) ) , ( (int(bl[3])*10) + int(bl[4]) ))

        def naa_istam(a, b, c, d):
            jvrc = 0

            for i in range(a, b+1):
                if c <= i <= d:
                    jvrc += 1
            
            return jvrc
        print(d1, d2, d3, d4)
        return max(naa_istam(d1, d2, d3, d4), naa_istam(d3, d4, d1, d2))

        


        

            
        