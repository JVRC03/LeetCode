class Solution:
    def exclusiveTime(self, n: int, arr: List[str]) -> List[int]:
        stack = []
        jvrc = [0] * n

        for i in range(len(arr)):
            a, b = '', ''
            for j in range(len(arr[i])):
                if arr[i][j] == ':':
                    break
                a += arr[i][j]
            
            for j in range(len(arr[i])-1, -1, -1):
                if arr[i][j] == ':':
                    break
                b += arr[i][j]
            b = b[::-1]

            if 'start' in arr[i]:
                stack.append([int(a), int(b)])
            else:
                x = stack.pop()
                temp = 1+int(b)-x[1]
                jvrc[int(a)] += (temp)
                if len(stack):
                    for j in range(len(stack)):
                        stack[j][-1] += temp

        return jvrc



        