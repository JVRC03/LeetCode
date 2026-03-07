class Solution:
    def exist(self, mat: List[List[str]], k: str) -> bool:
        self.jvrc = False

        def back_track(mat, i, j, k, idx):
            if idx >= len(k):
                self.jvrc = True
                return
            if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or self.jvrc or mat[i][j] == '0':
                return

            if k[idx] != mat[i][j]:
                return
            temp = mat[i][j]
            mat[i][j] = '0'
            back_track(mat, i, j+1, k, idx+1)
            back_track(mat, i, j-1, k, idx+1)
            back_track(mat, i+1, j, k, idx+1)
            back_track(mat, i-1, j, k, idx+1)
            mat[i][j] = temp

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == k[0]:
                    back_track(mat, i, j, k, 0)
                    if self.jvrc:
                        return True

        return self.jvrc


        