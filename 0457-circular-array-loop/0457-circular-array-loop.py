class Solution:

    def circularArrayLoop(self, nums: List[int]) -> bool:

        def f(a, b, k):
            while b:
                

                if not a:
                    a = k-1
                    b -= 1
                else:
                    b -= 1
                    a -= 1
            
            return a

        for i in range(len(nums)):
            temp = [0] * len(nums)
            temp[i] = 1
            s = i
            pos, neg = 0, 0

            while True: 
                prev = s
                if nums[s] < 0:
                    s = f(s, abs(nums[s]), len(nums))
                else:
                    s = (s+nums[s])%len(nums)
                if prev == s:
                    break
                   
                if nums[s] < 0:
                    if pos:
                        break
                    neg = 1
                else:
                    if neg:
                        break
                    pos = 1

                if temp[s] == 1:
                    if s == i:
                        return True
                    break
                
                temp[s] = 1
        

        return False

                


