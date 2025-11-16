# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], q: List[int]) -> List[List[int]]:
        arr, jvrc = [], []

        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
    
        def get(k):
            
            f, r = 0, len(arr)-1
            a, b = -1, -1
        
            while f <= r:
                mid = (f+r)//2

                if arr[mid] > k:
                    r = mid-1
                else:
                    a = arr[mid]
                    f = mid+1
            
            f, r = 0, len(arr)-1

            while f <= r:
                mid = (f+r)//2

                if arr[mid] < k:
                    f = mid+1
                else:
                    b = arr[mid]
                    r = mid-1

            return [a, b]

        for i in range(len(q)):
            jvrc.append(get(q[i]))
        
        return jvrc

        

        