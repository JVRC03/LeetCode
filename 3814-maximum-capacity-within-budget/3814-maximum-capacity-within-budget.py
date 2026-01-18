class Solution:
    def maxCapacity(self, a: List[int], b: List[int], k: int):
        heap, arr = [], []
        heapq.heapify(heap)

        for i in range(len(a)):
            heapq.heappush(heap, [a[i], b[i]])
        
        idx = 0
        while len(heap):
            temp = heapq.heappop(heap)

            a[idx] = temp[0]
            b[idx] = temp[1]

            idx += 1
        
        heap = []
        heapq.heapify(heap)

        for i in range(len(a)):
            heapq.heappush(heap, -b[i])

            x = abs(heapq.heappop(heap))
            y = -1

            if len(heap):
                y = abs(heapq.heappop(heap))
            
            if y == -1:
                arr.append([x, 0])
            else:
                arr.append([x, y])
            
            heapq.heappush(heap, -x)
            if y != -1:
                heapq.heappush(heap, -y)
        
        jvrc = 0

        def check(n, target):
            f, r = 0, len(arr)-1
            ans = 0

            while f <= r:
                mid = f + ((r-f) // 2)

                if a[mid] >= n:
                    r = mid-1
                else:
                    if target == arr[mid][0]:
                        ans = max(ans, arr[mid][1])
                    elif target == arr[mid][1]:
                        ans = max(ans, arr[mid][0])
                    else:
                        ans = max(ans, arr[mid][0], arr[mid][1])
                    f = mid+1
            
            return ans

        for i in range(len(a)):
            if a[i] < k:
                rem = k-a[i]

                jvrc = max(jvrc, b[i]+check(rem, b[i]))

        return jvrc

        