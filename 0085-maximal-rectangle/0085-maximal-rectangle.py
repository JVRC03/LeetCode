class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        pre = [0] * len(mat[0])
        def func(arr):
            left, right = [], []
            stack = []

            for i in range(len(arr)):
                if not len(stack):
                    stack.append(i)
                    left.append(i)
                    continue
                
                while len(stack) and arr[i] <= arr[stack[-1]]:
                    stack.pop()

                if not len(stack):
                    left.append(0)
                else:
                    left.append(stack[-1] + 1)
                
                stack.append(i)
            
            stack = []
            for i in range(len(arr) - 1, -1, -1):
                if not len(stack):
                    stack.append(len(arr) - 1)
                    right.append(len(arr) - 1)
                    continue
                
                while len(stack) and arr[i] <= arr[stack[-1]]:
                    stack.pop()
                
                if not len(stack):
                    right.append(len(arr) - 1)
                else:
                    right.append(stack[-1] - 1)
                
                stack.append(i)
            
            right = right[::-1]

            ans = 0
            for i in range(len(arr)):
                diff = (right[i] - left[i] + 1) * arr[i]
                ans = max(ans, diff)
            
            return ans

        jvrc = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == '1':
                    pre[j] += 1
                else:
                    pre[j] = 0
            
            jvrc = max(jvrc, func(pre))
        
        return jvrc







        