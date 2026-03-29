class EventManager:

    def __init__(self, arr: list[list[int]]):
        self.dic = {}
        self.heap = []
        heapq.heapify(self.heap)

        for i in range(len(arr)):
            heapq.heappush(self.heap, [-arr[i][1], arr[i][0]])
            self.dic[arr[i][0]] = arr[i][1]

    def updatePriority(self, a: int, b: int) -> None:
        self.dic[a] = b
        heapq.heappush(self.heap, [-b, a])

    def pollHighest(self) -> int:
        while len(self.heap):
            pair = heapq.heappop(self.heap)
            e_id, pri = pair[1], abs(pair[0])

            if e_id not in self.dic or self.dic[e_id] != pri:
                continue
            
            del self.dic[e_id]
            
            return e_id
        
        return -1
        
# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()