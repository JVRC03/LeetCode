class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        dic = {}
        tot, maxi = 0, 0

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = cost[i]
            else:
                dic[s[i]] += cost[i]
            
            tot += cost[i]
            maxi = max(maxi, dic[s[i]])
    

        return tot-maxi
        