# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        jvrc = 0
        arr = []

        while head != None:
            arr.append(head.val)
            head = head.next
        
        c = 0
        while len(arr):
            jvrc += int(math.pow(2, c)*(arr[-1]))
            c += 1
            arr.pop()
        
        return jvrc
        