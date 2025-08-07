class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic = {}
        arr.sort()

        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
        
        while len(dic):
            k = -1
            for i in dic:
                k = i
                break
            c = k//2

            if k == 0:
                if dic[0]%2 == 1:
                    return False
                del dic[0]
                continue

            if (k*2) in dic:
                dic[k] -= 1
                if not dic[k]:
                    del dic[k]
                k *= 2
                dic[k] -= 1
                if not dic[k]:
                    del dic[k]
            
            elif c in dic and c*2 == k:
                dic[c] -= 1
                if not dic[c]:
                    del dic[c]
                c *= 2
                dic[c] -= 1
                if not dic[c]:
                    del dic[c]
            else:
                return False
        
        return True