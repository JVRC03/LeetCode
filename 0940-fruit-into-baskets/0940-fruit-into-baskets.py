class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        jvrc = 0
        dic = {}
        f, r = 0, 0

        while f <= r and r < len(arr):
            if len(dic) == 2 and arr[r] not in dic:
                jvrc = max(jvrc, sum(dic.values()))
                while len(dic) == 2:
                    dic[arr[f]] -= 1
                    if not dic[arr[f]]:
                        del dic[arr[f]]
                    f += 1
            
            if arr[r] not in dic:
                dic[arr[r]] = 1
            else:
                dic[arr[r]] += 1
            r += 1

        if len(dic) <= 2:
            jvrc = max(jvrc, sum(dic.values()))
            
        return jvrc
            




        