class Solution:

    def __init__(self):
        self.jvrc = False
    
    def f(self, s, arr, idx):
        if self.jvrc == True:
            return 
        
        if len(arr) and arr[-1][0] == '0':
            c = arr[-1].count('0')
            if c != len(arr[-1]):
                return 

        if len(arr) > 2:
            if int(arr[-3])+int(arr[-2]) != int(arr[-1]):
                return
            
            if idx >= len(s):
                if int(arr[-3])+int(arr[-2]) == int(arr[-1]):
                    self.jvrc = True
                    return

        temp = ''

        for i in range(idx, len(s)):
            temp += s[i]
            arr.append(temp)
            self.f(s, arr, i+1)
            arr.pop()

    def isAdditiveNumber(self, s: str) -> bool:

        self.f(s, [], 0)

        return self.jvrc
        