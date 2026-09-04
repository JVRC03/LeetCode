class Solution:
    def longestStrChain(self, arr: List[str]) -> int:
        dic = {}
        arr.sort(key=len)

        for i in range(len(arr)):
            s = arr[i]
            curr = 1

            for j in range(len(s)):
                temp = s[0:j] + s[j+1:]

                if temp in dic:
                    curr = max(curr, 1 + dic[temp])

            dic[s] = curr
            
        return max(dic.values())
        