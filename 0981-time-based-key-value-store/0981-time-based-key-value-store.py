class TimeMap:

    def __init__(self):
        self.dic = {}
        self.ans = {}

    def set(self, key: str, value: str, k: int) -> None:
        if key not in self.dic:
            self.dic[key] = [k]
            self.ans[key] = [value]
        else:
            self.dic[key].append(k)
            self.ans[key].append(value)        

    def get(self, key: str, k: int) -> str:
        idx = -1
        if key not in self.dic:
            return ''
            
        arr = self.dic[key]

        f, r = 0, len(arr)-1

        while f <= r:
            mid = f + ((r - f) // 2)

            if arr[mid] > k:
                r = mid-1
            else:
                idx = mid
                f = mid+1
        
        if idx == -1:
            return ''
        
        return self.ans[key][idx]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)