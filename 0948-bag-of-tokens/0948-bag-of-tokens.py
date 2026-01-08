class Solution:
    def bagOfTokensScore(self, arr: List[int], k: int) -> int:
        arr.sort()
        f, r = 0, len(arr)-1
        curr, jvrc = 0, 0

        while f <= r:
            if k >= arr[f]:
                k -= arr[f]
                curr += 1
                f += 1
                continue
            
            if curr:
                jvrc = max(jvrc, curr)
                curr -= 1
                k += arr[r]
                r -= 1
                continue
                
            break
        
        jvrc = max(jvrc, curr)

        return jvrc
        