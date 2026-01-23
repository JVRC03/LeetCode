# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        f = head

        while f is not None:
            if f not in dic:
                dic[f] = 1
                f = f.next
                continue
            return True
        
        return False

        