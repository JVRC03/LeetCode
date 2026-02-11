class Solution:
    def minimumLengthEncoding(self, arr: List[str]) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(arr)):
            heapq.heappush(heap, [-len(arr[i]), arr[i]])
        
        arr = []

        while len(heap):
            a = heapq.heappop(heap)
            arr.append(a[-1])
        
        jvrc = 0
        s = set()

        def call(st):
            if st in s:
                return True

            burr = ''
            for i in range(len(st)-1, -1, -1):
                burr = st[i] + burr
                s.add(burr)
            
            return False

        for i in range(len(arr)):
            if call(arr[i]):
                continue
            
            jvrc += (len(arr[i])+1)
        
        return jvrc
        

        