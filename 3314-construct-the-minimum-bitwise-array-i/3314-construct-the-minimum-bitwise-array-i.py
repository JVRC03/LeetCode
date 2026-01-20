class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        jvrc = []

        for i in range(len(nums)):
            s = bin(nums[i])
            s = s[2:]
            arr = list(s)

            if arr[-1] == '0':
                jvrc.append(-1)
            else:
                idx = -1

                for j in range(len(arr)-1, -1, -1):
                    if arr[j] == '0':
                        break
                    idx = j
                
                arr[idx] = '0'
            
                temp = ''.join(arr)
                k = int(temp, 2)
                jvrc.append(k)
        
        return jvrc 
                


           
            





        