class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        jvrc = []
        s = set()

        for i in range(len(arr)):
            f, r = i+1, len(arr)-1

            while f < r:
                k = arr[i]+arr[f]+arr[r]
                temp = (arr[i], arr[f], arr[r])
                if k == 0:
                    if temp not in s:
                        s.add(temp)
                        jvrc.append(temp)
                    
                    r -= 1
                    f += 1
                elif k > 0:
                    r -= 1
                else:
                    f += 1

        return jvrc

        