class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = {}
        s = set()

        for i in range(len(words)):
            if words[i] not in dic:
                dic[words[i]] = 1
            else:
                dic[words[i]] += 1
        
        jvrc, curr = 0, 0
        print(dic)
        for i in dic:
            if i[0] == i[1]:
                if dic[i]%2 == 0:
                    jvrc += (dic[i]*2)
                else:
                    curr = 1
                    jvrc += ((dic[i]-1)*2)
            else:
                temp = ''
                temp += i[1]
                temp += i[0]

                if (temp in dic) and (temp not in s) and (i not in s):
                    s.add(temp)
                    s.add(i)
                    c = min(dic[i], dic[temp])
                    jvrc += ((c*2)*2)
                        
        
        if curr:
            jvrc += 2 

        return jvrc

        