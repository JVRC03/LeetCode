class Solution:
    def totalNumbers(self, arr: List[int]) -> int:
        s = set()

        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if i != j and i != k and j != k:
                        val = str(arr[i]) + str(arr[j]) + str(arr[k])
                        if int(val) % 2 == 0 and val[0] != '0':
                            s.add(val)
        
        return len(s)
        