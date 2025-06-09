class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        jvrc = set()
        main = []

        for i in range(len(nums)):
            c = 0
            temp = []
            for j in range(i, len(nums)):
                if nums[j]%p == 0:
                    c += 1

                temp.append(nums[j])

                if c > k:
                    break
                
                main.append(temp[:])
        
        for i in range(len(main)):
            s = ''
            for j in range(len(main[i])):
                s += str(main[i][j])
                s += '-'
            if s not in jvrc:
                jvrc.add(s)
        
        return len(jvrc)
        