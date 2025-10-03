class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}

        for i in range(len(arr)):
            c = arr[i]%k

            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        

        while len(dic):
            i = 0
            for p in dic:
                i = p
                break

            if i==0 or i*2 == k:
                if dic[i]%2 == 1:
                    return False
                del dic[i]
                continue
            
            c = k-i
            if c not in dic:
                return False
            
            if dic[c] != dic[i]:
                return False
            
            del dic[c]
            del dic[i]
        
        return True
                
       

    
        