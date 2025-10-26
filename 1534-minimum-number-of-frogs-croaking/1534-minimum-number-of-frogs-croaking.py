class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        temp = {}
        dic = {
            'c' : 0,
            'r' : 0,
            'o' : 0,
            'a' : 0,
            'k' : 0
        }
        jvrc = 0

        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = 1
            else:
                temp[s[i]] += 1
        
        if len(temp) != 5:
            return -1
        
        c = temp['c']
        for i in temp:
            if temp[i] != c:
                return -1
        
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

            arr = list(dic.values())
            for i in range(len(arr)-1):
                if arr[i] < arr[i+1]:
                    return -1
                    
            if len(dic) == 5:
                yes = 1

                for j in dic:
                    if dic[j] > 0:
                        continue
                    yes = 0
                    break
                if yes:
                    jvrc = max(jvrc, max(dic.values()))
                    for j in dic:
                        dic[j] -= 1
                    
        return jvrc
            

        
        