class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dic = {}
        arr = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(len(arr)):
                k = math.sqrt( math.pow( abs(arr[j][0]-arr[i][0]) ,2 ) + math.pow( abs(arr[j][1]-arr[i][1]) ,2 ) )
                if k == 0 and i != j:
                    return False
                dic[k] = 1

        if len(dic) == 3:
            return True
        
        return False