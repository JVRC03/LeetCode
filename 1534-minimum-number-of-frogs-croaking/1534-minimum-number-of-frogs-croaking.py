class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        dic = {
            'c' : 0,
            'r' : 0,
            'o' : 0,
            'a' : 0,
            'k' : 0
        }
        jvrc = 0

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

            arr = list(dic.values())
            for j in range(len(arr)-1):
                if arr[j] < arr[j+1]:
                    return -1

            yes = 1

            for j in dic:
                if dic[j] > 0:
                    continue
                yes = 0
                break
            if yes:
                jvrc = max(jvrc, max(arr))
                for j in dic:
                    dic[j] -= 1
                if i == len(s)-1:
                    c = dic['c']
                    for j in dic:
                        if dic[j] != c:
                            return -1
            else:
                if i == len(s)-1:
                    c = dic['c']
                    for j in dic:
                        if dic[j] != c:
                            return -1
                    
        return jvrc
            

        
        