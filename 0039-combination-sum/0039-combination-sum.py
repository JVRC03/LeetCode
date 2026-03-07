class Solution:
    def __init__(self):
        self.jvrc = []
        self.temp = set()

    def back_track(self, arr, k, curr):
        tot = sum(curr)

        if tot > k:
            return
        if tot == k:
            tem = curr.copy()
            tem.sort()

            m = tuple(tem)
            
            if m not in self.temp:
                self.jvrc.append(curr.copy())
                self.temp.add(m)
            return
        
        for i in range(len(arr)):
            curr.append(arr[i])
            self.back_track(arr, k, curr)
            curr.pop()

    def combinationSum(self, arr: List[int], k: int) -> List[List[int]]:
        self.back_track(arr, k, [])
       
        return self.jvrc
        