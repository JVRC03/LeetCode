# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or head == None:
            return head
        arr = []
        temp = head

        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        
        idx = len(arr) - k 

        if k >= len(arr):
            idx = k % len(arr)
            idx = len(arr) - idx

        temp = head
        n = len(arr)

        for i in range(n):
            temp.val = arr[(idx + i) % n]
            temp = temp.next
        
        return head









        