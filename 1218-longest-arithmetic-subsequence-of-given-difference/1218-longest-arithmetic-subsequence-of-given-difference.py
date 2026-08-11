class Solution:
    def longestSubsequence(self, arr: List[int], k: int) -> int:
        dic = {}

        for i in range(len(arr)):
            diff = arr[i] - k

            curr = 1
            if diff in dic:
                curr += dic[diff] 
            
            dic[arr[i]] = curr

        return max(dic.values())
        