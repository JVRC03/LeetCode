# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, arr: List[List[int]]) -> Optional[TreeNode]:
        s = set()
        dic = {}

        for i in range(len(arr)):
            s.add(arr[i][0])

            if arr[i][0] not in dic:
                dic[arr[i][0]] = TreeNode(arr[i][0])
            
            if arr[i][1] not in dic:
                dic[arr[i][1]] = TreeNode(arr[i][1])

            if arr[i][-1] == 1:
                dic[arr[i][0]].left = dic[arr[i][1]]
            else:
                dic[arr[i][0]].right = dic[arr[i][1]]
        
        for i in range(len(arr)):
            if arr[i][1] in s:
                s.remove(arr[i][1])
        
        val = list(s)
        val = val[0]

        return dic[val] 


            







        