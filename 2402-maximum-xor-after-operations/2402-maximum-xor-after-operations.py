class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        s = set()

        for i in range(len(nums)):
            k = bin(nums[i])
            k = k[2:]
            c = 0
            for j in range(len(k)-1, -1, -1):
                if k[j] == '1':
                    s.add(c)
                c += 1
        
        c, jvrc = 0, 0

        while len(s):
            if c in s:
                jvrc += int(math.pow(2, c))
                s.remove(c)
            
            c += 1
        
        return jvrc
        

        