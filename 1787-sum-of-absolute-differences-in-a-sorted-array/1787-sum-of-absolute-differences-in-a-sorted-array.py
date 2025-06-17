class Solution:
    def getSumAbsoluteDifferences(self, jvrc: List[int]) -> List[int]:
        p_sum = [jvrc[0]]

        for i in range(1, len(jvrc)):
            p_sum.append(p_sum[-1]+jvrc[i])
        
        for i in range(len(jvrc)):
            k = -1
            if i == 0:
                k = abs(((len(jvrc)-1)*jvrc[i])-(p_sum[-1]-p_sum[0]))
            elif i == len(jvrc)-1:
                k = abs( ((len(jvrc)-1)*jvrc[i]) - (p_sum[-2]) )
            else:
                r = abs(((len(jvrc)-i-1) * jvrc[i]) - (p_sum[-1]-p_sum[i]))
                l = abs((i * jvrc[i]) - p_sum[i-1])

                k = (l+r)

            jvrc[i] = k
        
        return jvrc
        