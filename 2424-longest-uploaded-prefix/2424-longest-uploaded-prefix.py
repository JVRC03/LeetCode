class LUPrefix:

    def __init__(self, n: int):
        self.curr = 0
        self.arr = [0] * n
        
    def upload(self, k: int) -> None:
        self.arr[k-1] = 1

        idx = -1

        if self.curr == 0:
            idx = 0
        else:
            idx = self.curr-1
        
        for i in range(idx, len(self.arr)):
            if self.arr[i] == 1:
                self.curr = i+1
                continue
            break

    def longest(self) -> int:
        return self.curr
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()