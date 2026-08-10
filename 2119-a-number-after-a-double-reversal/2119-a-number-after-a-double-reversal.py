class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        s = s[::-1]
        rev1 = int(s)

        s = str(rev1)
        s = s[::-1]
        rev2 = int(s)

        if rev2 == num:
            return True
        return False
        