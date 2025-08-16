class RangeFreqQuery:

    def __init__(self, nums: List[int]):
        self.dic = {}

        for i in range(len(nums)):
            if nums[i] not in self.dic:
                self.dic[nums[i]] = [i]
            else:
                self.dic[nums[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.dic:
            return 0

        arr = self.dic[value]
        if right < arr[0] or left > arr[-1]:
            return 0
        if right == arr[0]:
            return 1

        f, r = 0, len(arr)-1
        jv, rc = float('inf'), 0

        while f <= r:
            mid = (f+r)//2 

            if arr[mid] >= left:
                jv = min(jv, mid)
                r = mid-1
            else:
                f = mid+1

        f, r = 0, len(arr)-1
        t = arr[jv]
        if t > right:
            return 0

        while f <= r:
            mid = (f+r)//2 

            if arr[mid] <= right:
                rc = max(rc, mid)
                f = mid+1
            else:
                r = mid-1

        return abs(jv-rc)+1        

        