class Solution:
    def maxProbability(self, n, arr, wt, src, k):
        heap = [[-1, src]]
        heapq.heapify(heap)
        dic = {}

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][1]
            w = wt[i]

            if a not in dic:
                dic[a] = [[b, w]]
            else:
                dic[a].append([b, w])

            if b not in dic:
                dic[b] = [[a, w]]
            else:
                dic[b].append([a, w])
        
        dist = [0] * n
        dist[src] = 0

        while len(heap):
            x = heapq.heappop(heap)

            curr, node = abs(x[0]), x[1]

            if curr < dist[node]:
                continue
            
            if node in dic:
                a = dic[node]

                for i in range(len(a)):
                    cost = curr * a[i][1]

                    if cost > dist[a[i][0]]:
                        dist[a[i][0]] = cost
                        heapq.heappush(heap, [-cost, a[i][0]])
        
        return dist[k]



        