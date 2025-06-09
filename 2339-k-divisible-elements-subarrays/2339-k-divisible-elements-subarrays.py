class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        jvrc = set()

        for i in range(len(nums)):
            c = 0
            s = ''
            for j in range(i, len(nums)):
                if nums[j]%p == 0:
                    c += 1

                s += str(nums[j])
                s += '-'

                if c > k:
                    break
                
                jvrc.add(s)        

        return len(jvrc)
        