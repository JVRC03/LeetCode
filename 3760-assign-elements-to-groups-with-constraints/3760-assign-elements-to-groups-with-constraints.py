class Solution:
    def assignElements(self, nums: List[int], jvrc: List[int]) -> List[int]:
        check = {}

        for i in range(len(jvrc)):
            if jvrc[i] not in check:
                check[jvrc[i]] = i

        dic = {}
        arr = []
        k = max(nums)

        for i in range(k+1):
            arr.append([])

        for i in range(1, k+1):
            c = i
            for j in range(i, k+1, c):
                arr[j].append(i)

        for i in range(len(nums)):
            n = nums[i]
            if n in dic:
                continue
            
            dic[n] = arr[n]
            
        jvrc = []
        
        for i in range(len(nums)):
            if dic[nums[i]][-1] == 'Yes':
                jvrc.append(dic[nums[i]][-2])
                continue
            if dic[nums[i]][-1] == 'No':
                jvrc.append(-1)
                continue

            n = dic[nums[i]]
            mini = float('inf')

            for j in range(len(n)):
                if n[j] in check:
                    mini = min(mini, check[n[j]])
                    
            if mini == float('inf'):
                jvrc.append(-1)
                dic[nums[i]].append('No')
                continue

            dic[nums[i]].append(mini)
            dic[nums[i]].append('Yes')
            jvrc.append(mini)
        
        return jvrc




        