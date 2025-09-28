class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = {}
        maxi = 0

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        
        dic = {}
        jvrc = 0
      
        for i in d:
            if d[i] not in dic:
                dic[d[i]] = [i]
            else:
                dic[d[i]].append(i)

            maxi = max(maxi, len(dic[d[i]]) )
            
        curr = 0
        for i in dic:
            if len(dic[i]) == maxi:
                if curr < i:
                    curr = i
                    jvrc = ''.join(dic[i])
        
        return jvrc
        
        
        

        

        
        