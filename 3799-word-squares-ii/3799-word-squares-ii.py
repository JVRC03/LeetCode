class Solution:

    def __init__(self):
        self.jvrc = []

    def check(self, idx, t):
        arr = []

        for i in range(len(idx)):
            arr.append(t[idx[i]])

        top, left, right, bottom = arr[0], arr[1], arr[2], arr[3]

        if top[0] == left[0] and top[3] == right[0] and bottom[0] == left[3] and bottom[3] == right[3]:
            self.jvrc.append(arr)

    def f(self, arr, curr):
        if len(curr) == 4:
            self.check(curr, arr)
            return 

        for i in range(len(arr)):
            if i not in curr:
                curr.append(i)
                self.f(arr, curr)
                curr.pop()

    def wordSquares(self, arr: List[str]) -> List[List[str]]:

        arr.sort()
        self.f(arr, [])

        return self.jvrc
        