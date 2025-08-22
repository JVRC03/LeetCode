class Solution:
    def findAllRecipes(self, arr: List[str], ing: List[List[str]], sup: List[str]):
        jvrc = set()
        s = set(sup)

        while True:
            c = 0

            for i in range(len(ing)):
                k = 0
                for j in range(len(ing[i])):
                    if ing[i][j] in s:
                        k += 1
                    else:
                        break
                
                if k == len(ing[i]):
                    jvrc.add(arr[i])
                    if arr[i] not in s:
                        s.add(arr[i])
                        c = 1
            
            if not c:
                break
        
        return list(jvrc)

                


        