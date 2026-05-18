class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = deque([0])
        k, val = set(), set()
        jvrc = 0
        dic = {}

        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = [i]
            else:
                dic[arr[i]].append(i)

        while len(q):
            c = len(q)

            for ia in range(c):
                idx = q.popleft()

                if idx == len(arr) - 1:
                    return jvrc
                
                if idx + 1 < len(arr) and (idx + 1) not in k:
                    q.append(idx + 1)
                    k.add(idx + 1)
                if idx - 1 > -1 and (idx - 1) not in k:
                    q.append(idx - 1)
                    k.add(idx - 1)
                
                if arr[idx] in val:
                    continue
                
                val.add(arr[idx])
                temp = dic[arr[idx]]
                for i in range(len(temp)):
                    if temp[i] not in k:
                        q.append(temp[i])
                        k.add(temp[i])
            
            jvrc += 1
        
        return jvrc
        


        