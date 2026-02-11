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
        
        jvrc = ''
        s = set()

        def call(st):
            
            if st in s:
                return True

            a = list(st)     
            f = -1
            burr = ''

            for i in range(len(a)):
                burr = a[f] + burr
                f -= 1
                s.add(burr)
            
            return False

        for i in range(len(arr)):
            res = call(arr[i])

            if res:
                continue
            
            jvrc += '#'
            jvrc += arr[i]
        
        return len(jvrc)
        

        