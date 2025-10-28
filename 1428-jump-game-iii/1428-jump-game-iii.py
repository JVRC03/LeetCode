class Solution:
    def canReach(self, arr: List[int], idx: int) -> bool:
        k = set()

        for i in range(len(arr)):
            if arr[i] == 0:
                k.add(i)

        f = 0
        s = {idx}
        q = [[idx, arr[idx]]]

        while f < len(q):
            a = q[f][0]+q[f][1]
            b = q[f][0]-q[f][1]

            if a in k or b in k:
                return True

            if a < len(arr) and a not in s:
                q.append([a, arr[a]])
                s.add(a)
            if b >= 0 and b not in s:
                q.append([b, arr[b]])
                s.add(b)
            
            f += 1
        
        return False
            

        