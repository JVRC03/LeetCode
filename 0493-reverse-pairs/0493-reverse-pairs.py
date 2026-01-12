class Solution:

    def __init__(self):
        self.jvrc = 0


    def reversePairs(self, nums: List[int]) -> int:

        def mergeSort(arr, low, high):
            if low >= high:
                return arr[low:high+1]
            
            mid = (low + high) // 2

            a = mergeSort(arr, low, mid)
            b = mergeSort(arr, mid+1, high)

            x, y = 0, 0

            while x < len(a) and y < len(b):
                if a[x] > 2 * b[y]:
                    self.jvrc += (len(a) - x)
                    y += 1
                    continue
                x += 1

            temp = []
            f, r = 0, 0

            while f < len(a) and r < len(b):
                if a[f] <= b[r]:
                    temp.append(a[f])
                    f += 1
                    continue
                temp.append(b[r])
                r += 1
            
            while f < len(a):
                temp.append(a[f])
                f += 1
            
            while r < len(b):
                temp.append(b[r])
                r += 1
            
            return temp

        mergeSort(nums, 0, len(nums)-1)

        return self.jvrc

        