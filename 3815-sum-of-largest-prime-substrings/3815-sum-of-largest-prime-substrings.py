class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        heap = []
        heapq.heapify(heap)
        st = set()

        def f(k):
            n = int(math.sqrt(k))+1
            if k == 1:
                return False

            for i in range(2, n):
                if k%i == 0:
                    return False
            return True
        
        for i in range(len(s)):
            temp = ''
            for j in range(i, len(s)):
                temp += s[j]
                if f(int(temp)) and (int(temp) not in st):
                    st.add(int(temp))
                    heapq.heappush(heap, -int(temp))
        
        c, jvrc = 0, 0

        while len(heap):
            if c == 3:
                break
            jvrc += abs(heapq.heappop(heap))
            c += 1
        
        return jvrc
        