class Solution:
    def findRadius(self, arr: List[int], k: List[int]) -> int:
        arr.sort()
        k.sort()

        def dfs(arr, k, mid):
            temp = []

            for i in range(len(k)):
                a = k[i]-mid
                b = k[i]+mid

                temp.append([a, b])
                        
            def binn(n):
                f, r = 0, len(temp)-1

                while f <= r:
                    m = (f + r) // 2

                    if temp[m][0] <= n <= temp[m][1]:
                        return True
                    
                    if n > temp[m][1]:
                        f = m + 1
                    else:
                        r = m - 1
                    
                return False

            for i in range(len(arr)):
                if binn(arr[i]):
                    continue
                return False
            
            return True

        f, r = 0, max(arr[-1], k[-1])
        jvrc = float('inf')

        while f <= r:
            mid = (f + r) // 2

            if dfs(arr, k, mid):
                jvrc = min(jvrc, mid)
                r = mid-1
            else:
                f = mid+1
            
        return jvrc



        