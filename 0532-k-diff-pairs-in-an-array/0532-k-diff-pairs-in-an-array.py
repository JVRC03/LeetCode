class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        jvrc = 0
        s = set()

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        for i in range(len(nums)):
            if nums[i] not in s:
                a = nums[i]-k
                b = nums[i]+k
                c = 0

                if a in dic and (a not in s):
                    if k == 0:
                        if dic[a] > 1:
                            jvrc += 1
                            del dic[a]
                    else:
                        jvrc += 1
                    s.add(nums[i])
                    c = 1

                if b in dic and (b not in s):
                    if k == 0:
                        if dic[b] > 1:
                            jvrc += 1
                            del dic[b]
                    else:
                        jvrc += 1
                    s.add(nums[i])
                    c = 1
            
            
        
        return jvrc
            
        