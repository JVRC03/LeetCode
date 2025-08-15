class Solution:
    def sampleStats(self, arr: List[int]) -> List[float]:
        mode, c = 0, 0
        mean, mc = 0, 0
        mini, maxi = float('inf'), float('-inf')

        for i in range(len(arr)):
            if arr[i] > 0:
                mean += (i * arr[i])
                mc += arr[i]
                maxi = max(maxi, i)
                mini = min(mini, i)
            
            if arr[i] > c:
                c = arr[i]
                mode = i/1
        
        med = -1

        if mc%2 == 1:
            k = int(math.ceil(mc/2))
            temp = 0

            for i in range(len(arr)):
                temp += arr[i]
                if temp >= k:
                    med = i
                    break
        else:
            k = mc//2
            temp = 0
            for i in range(len(arr)):
                temp += arr[i]
                if temp > k:
                    med = i

                    if temp-1 >= k:
                        med += i
                    else:
                        for j in range(i+1, len(arr)):
                            if arr[j] != 0:
                                med += j
                                break
                       
                    med /= 2

                    break
                elif temp == k:
                    med = i
                    for j in range(i+1, len(arr)):
                        if arr[j] != 0:
                            med += j
                            break
                    med /= 2
                    break

        return [mini/1, maxi/1, mean/mc, med/1, mode]

        