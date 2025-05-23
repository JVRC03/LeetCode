class Solution:
    def findArray(self, nums: List[int]) -> List[int]:
        jvrc = [nums[0]]
        def f(k):
            s = ''
            while k:
                s += str(k%2)
                k //= 2
            
            return s[::-1]

        for i in range(1, len(nums)):
            a = f(nums[i-1])
            b = f(nums[i])

            x = max(len(a), len(b))-min(len(a), len(b))
            z = '0' * x

            if len(a) < len(b):
                a = z+a
            else:
                b = z+b
            if i == 1:
                print(a, b)
            ans, c = 0, 0

            for j in range(len(a)-1, -1, -1):
                if a[j] == '1':
                    if b[j] == '0':
                        ans += int(math.pow(2, c))
                else:
                    if a[j] == '0':
                        if b[j] == '1':
                            ans += int(math.pow(2, c))
                c += 1
            jvrc.append(ans)

        return jvrc 



        