class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        jvrc = [0 ,float('inf')]

        if num*num == num+1 or num*num == num+2:
            jvrc = [num, num]

        k = int(math.sqrt(num))+1

        for i in range(1, k+10):
            a = num//i
            b = math.ceil(num/i)

            if a*i == num+1 or a*i == num+2:
                diff = abs(a-i)
                n = abs(jvrc[0], jvrc[-1])

                if diff < n:
                    jvrc = [a, i]

            if b*i == num+1 or b*i == num+2:
                diff = abs(b-i)
                n = abs(jvrc[0] - jvrc[-1])

                if diff < n:
                    jvrc = [b, i]          

        return jvrc
        