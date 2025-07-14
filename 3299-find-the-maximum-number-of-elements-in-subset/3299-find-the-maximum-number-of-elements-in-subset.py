class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dic = {}
        maxi, jvrc = 0, 0

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

            maxi = max(maxi, nums[i])
        
        s = set()

        for i in range(len(nums)):
            if nums[i] == 1:
                s.add(nums[i])
                jvrc = max(jvrc, 1)
                continue
            if nums[i] not in s:
                c = 0
                curr = nums[i]
                n = 2

                while True:
                    if curr <= maxi:
                        if curr in dic:
                            if dic[curr] > 1:
                                c += 2
                                s.add(curr)
                            else:
                                c += 1
                                break
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                    
                    curr = int(math.pow(nums[i], n))
                    n *= 2

            jvrc = max(jvrc, c)

        return jvrc
        