class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        jvrc = [0]

        stack = [[arr[-1], len(arr) - 1]]

        for i in range(len(arr)-2, -1, -1):
            while len(stack) and stack[-1][0] <= arr[i]:
                stack.pop()
            
            if len(stack):
                jvrc.append(stack[-1][-1] - i)
            else:
                jvrc.append(0)
            
            stack.append([arr[i], i])

        return jvrc[::-1]
        