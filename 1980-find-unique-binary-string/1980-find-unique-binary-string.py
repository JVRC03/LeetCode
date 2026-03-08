class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        dic = {}

        for i in range(len(nums)):
            a = int(nums[i], 2)
            
            dic[a] = 1

        c = 0

        while c in dic:    
            c += 1

        k = bin(c)
        k = str(k[2:])

        rem = ''
        while len(rem)+len(k) < len(nums[0]):
            rem += '0'

        k = rem+k    

        return k    
        