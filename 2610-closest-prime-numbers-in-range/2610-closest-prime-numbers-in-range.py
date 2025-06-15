class Solution:

    def closestPrimes(self, l: int, r: int) -> List[int]:
        temp = [1] * (r+1)
        temp[0] = 0
        temp[1] = 0
        
        for i in range(2, int(math.sqrt(r))+1):
            c = i*i
            for j in range(c, len(temp), i):
                temp[j] = 0
        
        arr = []

        for i in range(l, r+1):
            if temp[i]:
                arr.append(i) 
        
        ans = float('inf')
        jvrc = [-1, -1]
 
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < ans:
                ans = (arr[i+1]-arr[i])
                jvrc = [arr[i], arr[i+1]]
        
        return jvrc


       





        