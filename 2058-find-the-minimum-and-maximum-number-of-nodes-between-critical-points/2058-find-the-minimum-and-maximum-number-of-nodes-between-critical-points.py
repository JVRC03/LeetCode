# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        prev = head
        head = head.next
        c = 1

        while head and head.next:
            if prev.val < head.val > head.next.val:
                arr.append(c)
            
            if prev.val > head.val < head.next.val:
                arr.append(c)
            
            prev = head
            head = head.next
            c += 1

        if not len(arr) or len(arr) == 1:
            return [-1, -1]
        
        jvrc = float('inf')
        for i in range(len(arr) - 1):
            jvrc = min(jvrc, arr[i + 1] - arr[i])
        
        return [jvrc, arr[-1] - arr[0]]
        


        