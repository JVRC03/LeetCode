# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        
        f, r = 0, len(arr) - 1
        
        jvrc = 0
        while f < r:
            jvrc = max(jvrc, arr[f] + arr[r])
            f += 1
            r -= 1
        
        return jvrc
        