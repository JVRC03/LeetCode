class Solution:
    def numOfBurgers(self, a: int, b: int) -> List[int]:
        if a%2 != 0 or b*4 < a or b > a:
            return []
        
        f, r = 0, b

        while f <= r:
            mid = (f+r)//2
            rem = b-mid
        
            k = (mid*2) + (rem*4)

            if k == a:
                return [rem, mid]
            
            if k > a:
                f = mid+1
            else:
                r = mid-1

        return []

        