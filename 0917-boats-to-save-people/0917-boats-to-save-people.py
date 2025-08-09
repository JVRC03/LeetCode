class Solution:
    def numRescueBoats(self, arr: List[int], k: int) -> int:
        arr.sort()
        jvrc = 0
        f, r= 0, len(arr)-1

        while f <= r:
            if arr[r] == k or arr[r]+arr[f] > k:
                r -= 1
                jvrc += 1
                continue
            f += 1
            r -= 1
            jvrc += 1
        
        return jvrc
        