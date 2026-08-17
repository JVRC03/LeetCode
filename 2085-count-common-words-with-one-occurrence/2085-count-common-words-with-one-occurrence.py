class Solution:
    def countWords(self, a: List[str], b: List[str]) -> int:
        dic = {}

        for i in range(len(a)):
            if a[i] not in dic:
                dic[a[i]] = '1'
            else:
                dic[a[i]] += '1'
        
        for i in range(len(b)):
            if b[i] not in dic:
                dic[b[i]] = '2'
            else:
                dic[b[i]] += '2'
        
        jvrc = 0
        for i in dic:
            if dic[i] == '12':
                jvrc += 1
        
        return jvrc
        