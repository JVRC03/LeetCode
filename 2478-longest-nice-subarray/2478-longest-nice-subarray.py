class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        jvrc = 0
        s = set()
        f, r = 0, 0

        def fa(k):
            c = 1
            a = bin(k)
            a = a[2:]

            for i in range(len(a)):
                if a[len(a)-i-1] == '1' and c in s:
                    return False
                c += 1
            c=1
            for i in range(len(a)-1, -1, -1):
                if a[i] == '1':
                    s.add(c)
                c+=1
            
            return True
        
        def change(k):
            c = 1
            while k:
                if k%2 == 1:
                    s.remove(c)
                c += 1
                k //= 2

        def check(k):
            c = 1
            while k:
                if k%2 == 1:
                    if c in s:
                        return False
                k //= 2
                c += 1

            return True
                
        while f <= r and r < len(nums):
            
            if fa(nums[r]):
                r += 1
                continue
            
            jvrc = max(jvrc, (r-f))

            while True:
                if check(nums[r]):
                    break
                change(nums[f])
                f += 1

            fa(nums[r])
            r += 1
    
        jvrc = max(jvrc, (r-f))
        
        return jvrc
                



                    



        
        