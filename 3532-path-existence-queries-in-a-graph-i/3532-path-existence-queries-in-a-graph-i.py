class Solution:
    def __init__(self):
        self.glob = -1

    def pathExistenceQueries(self, n: int, nums: List[int], k: int, q: List[List[int]]):
        dic, temp = {}, {}

        def check(val, f, arr, k):
            r = len(arr)-1
            ans = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid]-val > k:
                    r = mid-1
                else:
                    ans = mid
                    f = mid+1

            if ans == -1:
                return f-1
            
            return ans

        for i in range(n):
            temp[i] = check(nums[i], i+1, nums, k)
        
        vis = [0] * n

        def dfs(source):
            if vis[source]:
                return temp[source]
            
            vis[source] = 1
            ans = dfs(temp[source])
            self.glob = max(self.glob, ans)

            return self.glob
        s = set()

        for i in temp:
            if i == temp[i]:
                dic[i] = temp[i]
                continue
            
            if i in s:
                continue

            self.glob = -1
            dfs(i)

            j = i
            while j < self.glob:
                s.add(j)
                dic[j] = self.glob
                j += 1

        jvrc = []
 
        for i in range(len(q)):
            if q[i][-1] < q[i][0]:
                q[i][0], q[i][1] = q[i][1], q[i][0]

            if q[i][0] <= q[i][-1] <= dic[q[i][0]]:
                jvrc.append(True)
            else:
                jvrc.append(False)
        
        return jvrc
        
        
        
        
