class Solution:
    def maxPointsInsideSquare(self, arr: List[List[int]], s: str) -> int:
        jvrc = -1
        temp = {}
        f, r = 0, 0

        for i in range(len(arr)):
            r = max(r, abs(arr[i][0]), abs(arr[i][1]))
            k = str(arr[i][0]) + str(arr[i][1])
            temp[k] = s[i]
        
        arr.sort()
        s = ''

        for i in range(len(arr)):
            k = str(arr[i][0]) + str(arr[i][1])
            s += temp[k]

        def check(val, arr, s):
            st = set()
            curr = 0

            for i in range(len(arr)):
                if -val <= arr[i][0] and -val <= arr[i][1] and arr[i][0] <= val and arr[i][1] <= val:
                    if s[i] not in st:
                        st.add(s[i])
                        curr += 1
                        continue
                    return False, -1
            
            return True, curr

        while f <= r:
            mid = f + ((r - f) // 2)
            ans, local = check(mid, arr, s)
            if ans:
                jvrc = max(jvrc, local)
                f = mid+1
            else:
                r = mid-1
        
        return jvrc
        