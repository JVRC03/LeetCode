class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        dic = {}
        maxi = 0

        for i in range(len(nums)):
            s = bin(nums[i])
            s = s[2:]
            c = 0

            for j in range(len(s)-1, -1, -1):
                if s[j] == '1':
                    if c not in dic:
                        dic[c] = 1
                    else:
                        dic[c] += 1
                c += 1
                maxi = max(maxi, c)
        
        jvrc = 0
        k = len(nums)

        for i in range(len(nums)):
            s = bin(nums[i])
            s = s[2:]
            c = 0
            temp = '0' * (maxi-len(s))
            s = temp+s

            for j in range(len(s)-1, -1, -1):
                if s[j] == '0':
                    if c in dic:
                        jvrc += dic[c]
                else:
                    if c in dic:
                        jvrc += (k-dic[c])
                        dic[c] -= 1
                        if not dic[c]:
                            del dic[c]
                c += 1

            k -= 1
        
        return jvrc

        