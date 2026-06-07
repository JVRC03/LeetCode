class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        self.jvrc = []

        def check(arr):
            for i in range(len(arr) - 1):
                if arr[i] == arr[i + 1] == '1':
                    return -1
            
            cost = 0
            for i in range(len(arr)):
                if arr[i] == '1':
                    cost += i

            return cost

        def func(temp, idx, n, cost):
            if idx >= n:
                val = check(temp)
                if val != -1 and val <= cost:
                    self.jvrc.append(''.join(temp))
                return
            
            val = check(temp)
            if val != -1 and val <= cost:
                self.jvrc.append(''.join(temp))
            
            if val == -1:
                return

            for i in range(idx, n):
                temp[i] = '1'
                func(temp, i+1, n, cost)
                temp[i] = '0'

        func(['0'] * n, 0, n, k)

        return self.jvrc
        