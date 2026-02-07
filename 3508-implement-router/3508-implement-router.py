class Router:

    def __init__(self, k: int):
        self.q = deque([])
        self.tot = k
        self.dic = {}
        self.arr = {}

    def addPacket(self, source: int, destination: int, time: int) -> bool:

        temp = str(destination) + '-' + str(time)

        if (source in self.dic) and (temp in self.dic[source]):
            return False
        
        self.q.append([source, destination, time])

        if source not in self.dic:
            self.dic[source] = set()

        self.dic[source].add(temp)

        if destination not in self.arr:
            self.arr[destination] = deque([])
        self.arr[destination].append(time)
        
        if self.tot+1 == len(self.q):
            f = self.q.popleft()

            a = f[0]
            b = str(f[1]) + '-' + str(f[2])

            self.arr[f[1]].popleft()
            if not len(self.arr[f[1]]):
                del self.arr[f[1]]

            self.dic[a].remove(b)
            if not len(self.dic[a]):
                del self.dic[a]
        
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.q) == 0:
            return []
        
        a = self.q.popleft()
        
        source = a[0]
        k = str(a[1]) + '-' + str(a[2])

        self.dic[source].remove(k)
        self.arr[a[1]].popleft()

        if not len(self.arr[a[1]]):
            del self.arr[a[1]]

        if not len(self.dic[source]):
            del self.dic[source]

        return a
        
    def getCount(self, dest: int, st: int, et: int) -> int:
        if dest not in self.arr:
            return 0

        def check_min(arr, k):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] < k:
                    f = mid+1
                else:
                    r = mid-1
                    ans = mid
            
            return ans

        def check_max(arr, k):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = f + ((r - f) // 2)

                if arr[mid] <= k:
                    f = mid+1
                    ans = mid
                else:
                    r = mid-1
            
            return ans         
        
        a = check_min(self.arr[dest], st)
        b = check_max(self.arr[dest], et)

        if a == -1 or b == -1:
            return 0
        
        return (b-a)+1

        

        




        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)