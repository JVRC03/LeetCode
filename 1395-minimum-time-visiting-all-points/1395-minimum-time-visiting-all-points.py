class Solution:
    def minTimeToVisitAllPoints(self, arr: List[List[int]]) -> int:
        if len(arr) < 2:
            return 0
        
        jvrc = 0

        for i in range(len(arr)-1):
            a, b = arr[i][0], arr[i][-1]

            if a < arr[i+1][0] and b < arr[i+1][-1]:
                while a < arr[i+1][0] and b < arr[i+1][-1]:
                    a += 1
                    b += 1
                    jvrc += 1
            
                while a < arr[i+1][0]:
                    a += 1
                    jvrc += 1
                
                while b < arr[i+1][-1]:
                    b += 1
                    jvrc += 1
            
            elif a > arr[i+1][0] and b > arr[i+1][-1]:
                while a > arr[i+1][0] and b > arr[i+1][-1]:
                    a -= 1
                    b -= 1
                    jvrc += 1
            
                while a > arr[i+1][0]:
                    a -= 1
                    jvrc += 1
                
                while b > arr[i+1][-1]:
                    b -= 1
                    jvrc += 1
            else:

                if a > arr[i+1][0] and b < arr[i+1][1]:
                    while a > arr[i+1][0] and b < arr[i+1][1]:
                        a -= 1
                        b += 1
                        jvrc += 1
                    while a > arr[i+1][0]:
                        a -= 1
                        jvrc += 1
                    while b < arr[i+1][1]:
                        b += 1
                        jvrc += 1
                
                else:
                    if a < arr[i+1][0] and b > arr[i+1][1]:
                        while a < arr[i+1][0] and b > arr[i+1][1]:
                            a += 1
                            b -= 1
                            jvrc += 1
                        while a < arr[i+1][0]:
                            a += 1
                            jvrc += 1
                        while b > arr[i+1][1]:
                            b -= 1
                            jvrc += 1
                    else:
                        if a > arr[i+1][0]:
                            while a > arr[i+1][0]:
                                a -= 1
                                jvrc += 1
                        elif a < arr[i+1][0]:
                            while a < arr[i+1][0]:
                                a += 1
                                jvrc += 1
                        
                        if b > arr[i+1][-1]:
                            while b > arr[i+1][1]:
                                b -= 1
                                jvrc += 1
                        elif b < arr[i+1][-1]:
                            while b < arr[i+1][1]:
                                b += 1
                                jvrc += 1
        
        return jvrc
        