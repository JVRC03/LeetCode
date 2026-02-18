class Solution:
    def nearestExit(self, mat: List[List[str]], source: List[int]) -> int:
        q = deque([[source[0], source[1]]])

        s = set()

        self.jvrc = 1

        while len(q):
            c = len(q)

            for i in range(c):
                n = q.popleft()
                a, b = n[0], n[1]
                mat[a][b] = '+'
            
                if a < len(mat) and b+1 < len(mat[0]) and mat[a][b+1] == '.':
                    if a == 0 or a == len(mat)-1 or b+1 == len(mat[0])-1:
                        return self.jvrc
                    
                    if (a, b+1) not in s:
                        q.append([a, b+1])
                        s.add((a, b+1))
                
                if a < len(mat) and b-1 > -1 and mat[a][b-1] == '.':
                    if a == 0 or a == len(mat)-1 or b-1 == 0:
                        return self.jvrc

                    if (a, b-1) not in s:
                        q.append([a, b-1])
                        s.add((a, b-1))
                
                if a+1 < len(mat) and b < len(mat[0]) and mat[a+1][b] == '.':
                    if a+1 == len(mat)-1 or b == 0 or b == len(mat[0])-1:
                        return self.jvrc
                   
                    if (a+1, b) not in s:
                        s.add((a+1, b))
                        q.append([a+1, b])
            
                if a-1 > -1 and b < len(mat[0]) and mat[a-1][b] == '.':
                    if a-1 == 0 or b == 0 or b == len(mat[0])-1:
                        return self.jvrc
                    
                    if (a-1, b) not in s:
                        q.append([a-1, b])
                        s.add((a-1, b))
                
            self.jvrc += 1
        

        return -1
        