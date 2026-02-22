class Solution:
    def networkDelayTime(self, arr: List[List[int]], n: int, src: int) -> int:
        dic = {}
        heap = [[0, src-1]]
        heapq.heapify(heap)
        self.jvrc = 0

        for i in range(len(arr)):
            a, b = arr[i][0]-1, arr[i][1]-1
            wt = arr[i][2]

            if a not in dic:
                dic[a] = [[b, wt]]
            else:
                dic[a].append([b, wt])
        
        dist = [float('inf')] * n
        dist[src-1] = 0

        while len(heap):
            x = heapq.heappop(heap)

            curr, node = x[0], x[1]

            if node not in dic or curr > dist[node]:
                continue
            
            a = dic[node]

            for i in range(len(a)):
                cost = curr + a[i][-1]

                if cost < dist[a[i][0]]:
                    dist[a[i][0]] = cost
                    heapq.heappush(heap, [cost, a[i][0]])
        
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                return -1
            self.jvrc = max(self.jvrc, dist[i])

        return self.jvrc

        