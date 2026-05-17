class Solution:
    def canReach(self, arr: List[int], f: int) -> bool:
        q = deque([f])
        k = set()

        while len(q):
            c = len(q)

            for i in range(c):
                idx = q.popleft()

                if arr[idx] == 0:
                    return True

                k.add(idx)
                a, b = idx + arr[idx], idx - arr[idx]

                if a < len(arr) and a not in k:    
                    q.append(a)
                    k.add(a)
                if b > -1 and b not in k:
                    k.add(b)
                    q.append(b)

        return False       