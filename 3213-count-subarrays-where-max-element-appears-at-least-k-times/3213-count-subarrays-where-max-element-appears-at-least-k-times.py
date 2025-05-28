class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        jvrc = 0
        c = 0
        f, r = 0, 0
        maxi = max(nums)

        while f <= r and r < len(nums):
            if nums[r] == maxi:
                c += 1
            
            if c == k:
                while nums[f] != maxi:
                    jvrc += (len(nums)-r)
                    f += 1
                c -= 1
                f += 1
                jvrc += (len(nums)-r)
            r += 1

        return jvrc

        