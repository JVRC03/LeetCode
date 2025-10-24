class Solution:
    def __init__(self):
        self.jvrc = []

    def dfs(self, arr, curr, level):
        self.jvrc.append(curr)

        if curr == 1:
            return 
        
        a = int(math.pow(2, level-1))
        b = int(math.pow(2, level))-1
        diff = curr//2
        curr = a+(b-diff)

        level -= 1

        self.dfs(arr, curr, level)

    def pathInZigZagTree(self, k: int):
        arr = []

        for i in range(21):
            arr.append(int(math.pow(2, i)))
        
        def get_level(a):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = (f+r)//2

                if arr[mid] <= a:
                    ans = mid
                    f = mid+1
                else:
                    r = mid-1
            
            return ans

        level = get_level(k)
        self.dfs(arr, k, level)

        return self.jvrc[::-1]
        



        