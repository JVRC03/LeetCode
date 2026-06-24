class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
        
        s = set()
        for i in dic:
            if dic[i] in s:
                return False
            s.add(dic[i])
    
        return True
        