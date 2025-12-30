class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int):
        temp, o, z = [], [], []
        jvrc = 0

        for i in range(len(nums)):
            if l <= nums[i] <= r:
                temp.append(1)
                o.append(i)
                continue
            
            if nums[i] < l:
                temp.append(-1)
            else:
                temp.append(0)
                z.append(i)
        
        o = o[::-1]
        z = z[::-1]

        for i in range(len(nums)):
            if temp[i] == 0:
                if len(z):
                    z.pop()
            
            elif temp[i] == 1:
                if len(z):
                    jvrc += (z[-1]-i)
                else:
                    jvrc += (len(nums)-i)

                o.pop()
            else:
                if len(o):
                    if len(z):
                        if o[-1] < z[-1]:
                            jvrc += (z[-1]-o[-1])
                    else:
                        jvrc += (len(nums)-o[-1])
        
        return jvrc
            

        


        

        