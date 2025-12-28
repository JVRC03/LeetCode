class Solution:
    def missingRolls(self, arr: List[int], mean: int, n: int) -> List[int]:
        tot = mean * (n + len(arr))
        tot -= sum(arr)

        temp = tot/n

        if temp > 6 or temp < 1:
            return []
        
        temp = tot//n

        jvrc = [temp] * n
        
        if temp*n != tot:
            diff = tot-(temp*n)
            for i in range(len(jvrc)):
                if not diff:
                    break
                for j in range(6):
                    if not diff or jvrc[i] == 6:
                        break
                    jvrc[i] += 1
                    diff -= 1
                    

        return jvrc

        