class Solution:
    def findDisappearedNumbers(self, nums: list[int], a: int, b: int) -> list[list[int]]:
        k = set(nums)

        jvrc = []
        low, high = -1, -1
        for i in range(a, b + 1):
            if i not in k:
                if low == -1:
                    low = i
                high = i
            else:
                if low != -1:
                    jvrc.append([low, high])
                low, high = -1, -1
        
        if low != -1:
            jvrc.append([low, high])
                
        return jvrc


        