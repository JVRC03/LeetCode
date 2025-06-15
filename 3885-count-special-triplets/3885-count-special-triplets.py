class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        
        jvrc = 0 

        def f(k, arr):
            f, r = 0, len(arr)-1
            ans = -1

            while f <= r:
                mid = (f+r)//2

                if arr[mid] > k:
                    r = mid-1
                    ans = mid
                else:
                    f = mid+1

            return ans

        for i in range(len(nums)):
            temp = nums[i]*2

            if temp in dic:
                a = f(i, dic[temp])
                
                arr = dic[temp]
                r = len(dic[temp])-a
                l = 0

                if a-1 >= 0:
                    if arr[a-1] != i:
                        l = a
                    else:
                        if a-2 >= 0:
                            l = a-1

                jvrc += (l*r)

        return jvrc%1000000007


        