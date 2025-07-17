class Solution:
    def maxWeight(self, arr: List[int]) -> int:
        arr.sort()

        jvrc = 0
        k = len(arr)//4
        k = math.ceil(k/2)
        temp = k

        while temp:
            temp -= 1
            jvrc += arr.pop()
        
        arr = arr[::-1]

        temp = (3*k)

        while temp:
            temp -= 1
            arr.pop()

        arr = arr[::-1]

        while len(arr):
            arr.pop()
            jvrc += arr.pop()
            arr.pop(0)
            arr.pop(0)
        
        return jvrc



        