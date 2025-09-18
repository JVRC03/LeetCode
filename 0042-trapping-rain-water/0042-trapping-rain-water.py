class Solution:
    def trap(self, arr: List[int]) -> int:
        mx = arr.index(max(arr))

        jvrc = 0
        lx, rx = arr[0], arr[-1]

        for i in range(mx):
            lx = max(lx, arr[i])
            jvrc += (lx-arr[i])
        
        for i in range(len(arr)-1, mx, -1):
            rx = max(rx, arr[i])
            jvrc += (rx-arr[i])     

        return jvrc   
        