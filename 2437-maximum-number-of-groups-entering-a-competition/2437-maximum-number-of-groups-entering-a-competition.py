class Solution:
    def maximumGroups(self, arr: List[int]) -> int:
        jvrc, c = 0, 1

        while len(arr):
            success = 0
            temp = c

            while temp:
                if len(arr) == 0:
                    success = 0
                    break
                arr.pop()
                temp -= 1
                success = 1
            
            if success:
                c += 1
                jvrc += 1
        
        return jvrc

        

        