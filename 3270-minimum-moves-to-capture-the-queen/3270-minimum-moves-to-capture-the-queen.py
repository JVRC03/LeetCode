class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int):

        x, y = 0, 0

        if a == c == e:
            if b < d < f or b > d > f:
                return 2
            return 1
        
        if b == d == f:
            if  a < c < e or a > c > e:
                return 2
            return 1

        if abs(a-e) >= 1:
            x = 1
        if abs(b-f) >= 1:
            y = 1
        
        if (x+y) == 1:
            return 1

        if abs(a-c) == abs(b-d) and abs(a-e) == abs(b-f):
            if  c <= a <= e or c >= a >= e:
                return 2
            if  d <= b <= f or d >= b >= f:
                return 2           
            
            return 1
            
        if abs(c-e) == abs(d-f):
            return 1
            
        return 2
