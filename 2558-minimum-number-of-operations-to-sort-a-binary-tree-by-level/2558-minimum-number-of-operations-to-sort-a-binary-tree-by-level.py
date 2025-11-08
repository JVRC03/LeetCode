# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        jvrc = 0

        q = deque([root])

        while len(q):
            c = len(q)
            arr = []
            dic = {}

            for i in range(c):
                k = q.popleft()
                arr.append(k.val)
                dic[k.val] = i

                if k.left:
                    q.append(k.left)
                    
                if k.right:
                    q.append(k.right)
                    
            
            temp = arr.copy()
            arr.sort()

            for i in range(len(arr)):
                if arr[i] == temp[i]:
                    continue
                jvrc += 1
                vas = dic[arr[i]]
                dic[temp[i]] = vas
                temp[i], temp[vas] = temp[vas], temp[i]
                


        return jvrc
        