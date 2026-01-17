class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        jvrc = []

        def fill(main, curr):
            temp, idx = '', 0

            for i in range(len(curr)):
                if i < len(main):
                    temp += main[i]
            
            w=[]
            if temp == curr:
                w.append(0)
            
            idx += 1

            for i in range(len(curr), len(main)):
                temp += main[i]
                if temp[idx:] == curr:
                    w.append(idx)
                
                idx += 1
            
            return w

        x = fill(s, a)
        y = fill(s, b)

        def check(aa, bb):
            f, r = 0, len(y)-1

            while f <= r:
                mid = (f + r) // 2

                if aa <= y[mid] <= bb:
                    return True
                
                if y[mid] < aa:
                    f = mid+1
                else:
                    r = mid-1
            
            return False

        for i in range(len(x)):
            p = x[i] - k
            q = x[i] + k

            if check(p, x[i]) or check(x[i], q):
                jvrc.append(x[i])
        
        return jvrc

        