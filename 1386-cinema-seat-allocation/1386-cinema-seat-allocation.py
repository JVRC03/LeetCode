class Solution:
    def maxNumberOfFamilies(self, n: int, arr: List[List[int]]) -> int:
        arr.sort()
        jvrc = 0
        i = 0

        while i < len(arr):
            temp = set()
            n -= 1
            curr = arr[i][0]

            while i < len(arr) and arr[i][0] == curr:
                temp.add(arr[i][1])
                i += 1
            
            if len(temp):
                if (2 not in temp and 3 not in temp and 4 not in temp and 5 not in temp) and (6 not in temp and 7 not in temp and 8 not in temp and 9 not in temp):
                    jvrc += 2
                elif (2 not in temp and 3 not in temp and 4 not in temp and 5 not in temp):
                    jvrc += 1
                elif (4 not in temp and 5 not in temp and 6 not in temp and 7 not in temp):
                    jvrc += 1
                elif (6 not in temp and 7 not in temp and 8 not in temp and 9 not in temp):
                        jvrc += 1

        return jvrc + (n * 2)


            


        