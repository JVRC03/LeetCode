class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        jvrc, left = [], []
        
        def all_poss(arr):
            a = []
            glob = ''

            for i in range(len(arr)):
                sa = glob+arr[i]
                glob += arr[i]
                if sa[0] == '0' and len(sa) > 1:
                    continue
                if i != len(arr)-1:
                    sa += '.'
                
                x = 0
                tot = 0
                hehe = ''
                for j in range(i+1, len(arr)):
                    sa += arr[j]
                    if arr[j] == '0':
                        x += 1
                    tot += 1
                    hehe += arr[j]
                if x == tot and tot > 0:
                    continue   

                if len(hehe) and hehe[-1] == '0':
                    continue  


                
                a.append(sa)
            
            return a

        for i in range(2, len(s)-1):
            left.append(s[i-1])
            
            right = []
            for j in range(i, len(s)-1):
                right.append(s[j])
            
            x = all_poss(left)
            y = all_poss(right)
            temp = []
            for j in range(len(x)):
                curr = []
                for k in range(len(y)):
                    sa = '('
                    sa += x[j]
                    sa += ', '
                    sa += y[k]
                    sa += ')'
                    curr.append(sa)
                temp.extend(curr)
            
            jvrc.extend(temp)
        
        return jvrc



            



        